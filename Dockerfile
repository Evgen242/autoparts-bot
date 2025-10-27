# ---------- Stage 1: builder (ставим зависимости отдельно) ----------
FROM python:3.11-slim AS builder

# Обновление пакетов безопасности (минимально)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
  && rm -rf /var/lib/apt/lists/*

# Рабочая директория для сборки
WORKDIR /app

# Копируем только requirements для лучшего кеширования
COPY requirements.txt /app/requirements.txt

# Ставим зависимости без кеша и компиляции лишнего
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# ---------- Stage 2: runtime (чистый рантайм) ----------
FROM python:3.11-slim

# Создаём непривилегированного пользователя
ARG APP_USER=appuser
ARG APP_UID=10001
RUN useradd -u ${APP_UID} -m ${APP_USER}

# Рабочая директория рантайма
WORKDIR /app

# Переменные окружения для Python (улучшают поведение в контейнере)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Копируем зависимости из builder-образа (слой с установленными пакетами)
# Прим: пакеты уже внутри системного site-packages builder-а, поэтому проще переустановить в рантайме.
# Однако для простоты и читаемости — ставим зависимости заново (они кешируются Docker-демоном).
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . /app

# Меняем владельца файлов
RUN chown -R ${APP_USER}:${APP_USER} /app

# Переходим на непривилегированного пользователя
USER ${APP_USER}

# Старт приложения
# Если у тебя файл называется bot.py — оставляем так.
CMD ["python", "bot.py"]
