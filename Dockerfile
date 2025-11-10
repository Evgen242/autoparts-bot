FROM python:3.11-slim

WORKDIR /app

# Копируем только requirements сначала для лучшего кэширования
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем только необходимые файлы
COPY bot.py database.py ./

# Создаем пользователя для безопасности
RUN useradd -m -u 1000 botuser && chown -R botuser:botuser /app
USER botuser

CMD ["python", "bot.py"]
