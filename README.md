# Тестовое задание

Создать и активировать виртуальное окружение:

    python3 -m venv venv

    source venv/bin/activate

Установка зависимостей:

    pip install -r requirements.txt

Запуск проекта

    python3 manage.py runserver

## Точки входа.

БюСписок товаров:

    /api/products/

Конкретный товар:

    /api/products/<int:pk>

