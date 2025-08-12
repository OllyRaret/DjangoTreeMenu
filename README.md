# Древовидное меню для Django

## Описание

Django-приложение для создания и управления многоуровневыми меню с возможностью:
- Неограниченной вложенности пунктов
- Автоматического определения активного пункта по URL
- Редактирования через стандартную админку Django
- Быстрой отрисовки в шаблонах

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/OllyRaret/DjangoTreeMenu.git
cd DjangoTreeMenu
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл .env в корне проекта со следующим содержимым:

```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

5. Настройте базу данных (по умолчанию SQLite):
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

7. Запустите сервер:
```bash
python manage.py runserver
```

## Примеры URL
- Главная страница меню: http://127.0.0.1:8000/catalog/
- Конкретный пункт меню: http://127.0.0.1:8000/catalog/11/ (где 11 - ID пункта)
- При этом автоматически раскроется:
  - Все родительские пункты
  - Первый уровень вложенных пунктов

![Пример меню](/docs/menu-screenshot.png)

## Особенности работы
- Все меню отрисовываются за 1 запрос к БД
- Активный пункт определяется автоматически по URL
- Включены готовые CSS-стили для красивого отображения

