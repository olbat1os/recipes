# Приложение рецептов блюд

Фуллстек-приложение для просмотра рецептов блюд, построенное на Django REST Framework и React.

## Установка и запуск

### Бэкенд (Django)

1. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Примените миграции:
```bash
cd backend
python manage.py migrate
```

4. Запустите сервер разработки:
```bash
python manage.py runserver
```

### Фронтенд (React)

1. Установите зависимости:
```bash
cd frontend
npm install
```

2. Запустите сервер разработки:
```bash
npm start
```

## Документация API

Документация API доступна по адресу: http://localhost:8000/swagger/ 
