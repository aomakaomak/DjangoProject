# Базовый образ Python
FROM python:3.9

# Рабочая директория в контейнере
WORKDIR /app

# Немного удобных настроек для Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Устанавливаем Poetry (и обновляем pip)
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir poetry

# Копируем файлы с зависимостями Poetry
# ОЖИДАЕМ, ЧТО В КОРНЕ ПРОЕКТА ЕСТЬ pyproject.toml И poetry.lock
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости через Poetry
# virtualenvs.create=false — чтобы пакеты ставились в системное окружение контейнера,
# а не во внутренний venv, иначе потом "python manage.py" их не увидит.
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Копируем остальной код проекта
COPY . .

# Открываем порт 8000
EXPOSE 8000

# Команда запуска (аналогична твоей)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
