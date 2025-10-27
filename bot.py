import logging
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
import database as db
from sqlalchemy.orm import Session
from sqlalchemy import func
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING)
logger = logging.getLogger(__name__)

# Состояния для ConversationHandler
ADD_PART = 1

# Клавиатуры
main_keyboard = ReplyKeyboardMarkup([
    ['/add', '/search'],
    ['/list', '/stats']
], resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '🚗 Добро пожаловать в бот учета автозапчастей!\n\n'
        'Команды:\n'
        '/add - Добавить запчасть\n'
        '/search - Поиск запчасти\n'
        '/list - Список всех запчастей\n'
        '/stats - Статистика\n'
        '/cancel - Отмена операции',
        reply_markup=main_keyboard
    )

async def add_part_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Введите данные запчасти в формате:\n\n'
        'Название\n'
        'Марка автомобиля\n'
        'Модель автомобиля\n'
        'Номер запчасти\n'
        'Количество\n'
        'Цена\n'
        'Место хранения\n'
        'Описание\n\n'
        'Пример:\n'
        'Тормозной диск\n'
        'Toyota\n'
        'Camry\n'
        '43512-06060\n'
        '2\n'
        '4500\n'
        'Стеллаж А1\n'
        'Новый, оригинал\n\n'
        'Или напишите /cancel для отмены',
        reply_markup=ReplyKeyboardRemove()
    )
    return ADD_PART

async def add_part_process(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = update.message.text.split('\n')
        if len(data) < 7:
            await update.message.reply_text('❌ Недостаточно данных. Нужно минимум 7 строк! Попробуйте снова:')
            return ADD_PART
        
        # Создаем запчасть
        part = db.AutoPart(
            name=data[0].strip(),
            car_brand=data[1].strip(),
            car_model=data[2].strip(),
            part_number=data[3].strip(),
            quantity=int(data[4].strip()),
            price=float(data[5].strip()),
            location=data[6].strip(),
            description=data[7].strip() if len(data) > 7 else ''
        )
        
        # Сохраняем в базу
        session = db.Session()
        session.add(part)
        session.commit()
        session.close()
        
        await update.message.reply_text('✅ Запчасть успешно добавлена!', reply_markup=main_keyboard)
        return ConversationHandler.END
        
    except ValueError:
        await update.message.reply_text('❌ Ошибка в формате чисел (количество или цена). Попробуйте снова:')
        return ADD_PART
    except Exception as e:
        await update.message.reply_text(f'❌ Ошибка: {e}\nПопробуйте снова:', reply_markup=main_keyboard)
        return ConversationHandler.END

async def search_part(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text('🔍 Введите что искать: /search <текст>')
        return
    
    search_text = ' '.join(context.args)
    session = db.Session()
    
    try:
        # Ищем по всем полям
        results = session.query(db.AutoPart).filter(
            (db.AutoPart.name.ilike(f'%{search_text}%')) |
            (db.AutoPart.car_brand.ilike(f'%{search_text}%')) |
            (db.AutoPart.car_model.ilike(f'%{search_text}%')) |
            (db.AutoPart.part_number.ilike(f'%{search_text}%'))
        ).all()
        
        if not results:
            await update.message.reply_text('❌ Ничего не найдено')
            return
        
        response = f'🔍 Найдено запчастей: {len(results)}\n\n'
        for part in results:
            response += (
                f'🏷️ {part.name}\n'
                f'🚗 {part.car_brand} {part.car_model}\n'
                f'🔢 Номер: {part.part_number}\n'
                f'📦 Количество: {part.quantity}\n'
                f'💰 Цена: {part.price} руб.\n'
                f'📍 Место: {part.location}\n'
                f'📝 {part.description}\n'
                f'────────────────────\n'
            )
        
        # Разбиваем сообщение если слишком длинное
        if len(response) > 4000:
            for i in range(0, len(response), 4000):
                await update.message.reply_text(response[i:i+4000])
        else:
            await update.message.reply_text(response)
            
    finally:
        session.close()

async def list_parts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    session = db.Session()
    
    try:
        parts = session.query(db.AutoPart).all()
        if not parts:
            await update.message.reply_text('📦 База данных пуста')
            return
        
        response = f'📋 Всего запчастей: {len(parts)}\n\n'
        for part in parts:
            response += f'• {part.name} ({part.car_brand} {part.car_model}) - {part.quantity} шт.\n'
        
        await update.message.reply_text(response)
        
    finally:
        session.close()

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    session = db.Session()
    
    try:
        total_parts = session.query(db.AutoPart).count()
        total_quantity = session.query(func.sum(db.AutoPart.quantity)).scalar() or 0          
        unique_brands = session.query(db.AutoPart.car_brand).distinct().count()
        total_value = session.query(func.sum(db.AutoPart.price * db.AutoPart.quantity)).scalar() or 0
        
        response = (
            f'📊 Статистика:\n\n'
            f'• Всего позиций: {total_parts}\n'
            f'• Общее количество: {total_quantity} шт.\n'
            f'• Уникальных марок: {unique_brands}\n'
            f'• Общая стоимость: {total_value:.2f} руб.'
        )
        
        await update.message.reply_text(response)
        
    finally:
        session.close()

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('❌ Операция отменена', reply_markup=main_keyboard)
    return ConversationHandler.END

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f'Update {update} caused error {context.error}')

def main():
    # Инициализация базы данных
    db.init_db()
    
    # Создаем Application
    application = Application.builder().token(TOKEN).build()
    
    # ConversationHandler для добавления запчасти
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('add', add_part_start)],
        states={
            ADD_PART: [MessageHandler(filters.TEXT & ~filters.COMMAND, add_part_process)]
        },
        fallbacks=[CommandHandler('cancel', cancel)],
        allow_reentry=True
    )
    
    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("search", search_part))
    application.add_handler(CommandHandler("list", list_parts))
    application.add_handler(CommandHandler("stats", stats))
    application.add_handler(CommandHandler("cancel", cancel))
    
    application.add_error_handler(error_handler)
    
    # Запускаем бота
    logger.info("Бот запущен!")
    application.run_polling()

if __name__ == '__main__':
    main()
