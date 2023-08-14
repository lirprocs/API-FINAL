# Установка Python
FROM python:3.10-slim

# Установка рабочего каталога
WORKDIR /app
ENV PYTHONPATH=/app
ENV SQLALCHEMY_DATABASE_URL="postgresql+asyncpg://docker:password@db/restoran"

# Установка зависимостей
COPY requirements.txt /app/

# Установка переменных среды
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY . /app/

# Запуск приложения
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
