# Construction Company API  
API для управления строительной компанией: проекты, здания, клиенты, подрядчики.

---

## Технологии

| Технология | Использование |
|-----------|--------------|
| Django  | Web backend |
| Django REST Framework | API |
| drf-yasg | Swagger документация |
| JWT (SimpleJWT) | Авторизация |
| PostgreSQL / SQLite | База данных |
| Docker / Docker Compose | Контейнеризация |

---

## Установка и запуск

### 1. Клонирование репозитория

git clone <repository-url>
cd construction-api

### 2. Создать виртуальное окружение
Windows:
python -m venv venv
venv\Scripts\activate

Linux/macOS:
python3 -m venv venv
source venv/bin/activate

### 3. Установить зависимости
pip install -r requirements.txt

### 4. Настроить переменные окружения
Создай .env:

SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3

### 5. Применить миграции
python manage.py migrate

### 6. Создать суперпользователя
python manage.py createsuperuser

### 7. Запуск сервера
python manage.py runserver

Авторизация

Используется JWT (SimpleJWT).

Получить токен:

POST /api/token/

{
  "username": "admin",
  "password": "password"
}

Использование:

В Swagger:
Bearer <access_token>

