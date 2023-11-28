# Visited Links Service

Этот проект представляет собой простой веб-сервис для учета посещенных ресурсов.

## Технические требования

- Python 3
- Django
- SQLite

## Установка

1. Клонируйте репозиторий:

    
    git clone https://github.com/Yasuo20012001/visited_links_service.git
    

2. Перейдите в каталог проекта:

    
    cd visited_links_service
    

3. Установите зависимости:

    
    pip install -r requirements.txt
    

4. Примените миграции:

    
    python manage.py migrate
    

## Запуск

1. Запустите сервер:

    
    python manage.py runserver
    

2. Сервер будет доступен по адресу http://127.0.0.1:8000/.

## Использование

### Добавление посещенных ссылок

Отправьте POST-запрос с JSON-данными вида:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"links":["https://ya.ru/", "https://sber.ru"]}' http://127.0.0.1:8000/visited_links/
