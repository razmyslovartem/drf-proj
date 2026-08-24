FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DOCKER_CONTAINER=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VERSION=2.3.0

WORKDIR /app

# Устанавливаем системные зависимости для psycopg2 (если используете PostgreSQL)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем poetry
RUN pip install --no-cache-dir poetry==${POETRY_VERSION}

# Копируем только файлы с зависимостями (для кеширования слоя)
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости (только основные, без dev)
RUN poetry install --only main --no-interaction --no-root

# Копируем весь остальной проект
COPY . .

# Открываем порт
EXPOSE 8000

# Команда запуска: сначала миграции, потом сервер
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
