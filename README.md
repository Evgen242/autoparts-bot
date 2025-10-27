# AutoLot25 Telegram Bot

🚗 Telegram-бот для учёта автозапчастей.  
Поддерживает добавление, поиск, список и статистику.

## 📦 Возможности
- `/add` — добавить запчасть  
- `/search` — поиск по названию, бренду, модели или номеру  
- `/list` — список всех запчастей  
- `/stats` — статистика (количество, бренды, стоимость)

## 🚀 Запуск через Docker
```bash
git clone https://github.com/USERNAME/autoparts-bot.git
cd autoparts-bot
cp .env.example .env   # заполнить токен и параметры БД
docker compose up -d --build
🛠️ Стек
Python 3.11

python-telegram-bot

SQLAlchemy

PostgreSQL

Docker + docker-compose

