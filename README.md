# YaMDb API
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)

Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий может быть расширен. Пользователи оставляют к произведениям текстовые отзывы и выставляют произведению рейтинг. Из множества оценок автоматически высчитывается средняя оценка произведения. К отзывам на прозведения другие пользователи могут оставлять комментарии.<br>
YaMDb - это REST API проект, для отправки запросов можно использовать инструмент [Postman](https://www.postman.com/downloads/) или аналогичные сервисы.<br>
Техническое описание, шаблоны запросов и структура ответов проекта доступны после запуска приложения по адресу [localhost:8000/redoc/](http://localhost:8000/redoc/).

## Запуск и развертывание приложения
- Cклонируйте данный репозиторий:
    ```bash
    git clone https://github.com/russel-07/yamdb_api-project.git
    ```

- Откройте проект, создайте и запустите виртуальное окружение:
    ```bash
    python -m venv venv && source venv/Scripts/activate
    ```

- Установите пакеты виртуального окружения:
    ```bash
    pip install -r requirements.txt
    ```

- Выполните миграции:
    ```bash
    python manage.py migrate
    ```

- При необходимости заполните базу данных тестовыми данными из файла 'fixtures.json':
    ```bash
    python manage.py loaddata fixtures.json
    ```

- Создайте суперпользователя:
    ```bash
    python manage.py createsuperuser
    ```

- Запустите проект:
    ```bash
    python manage.py runserver
    ```

- Приложение будет запущено в режиме отладки с эмуляцией почтового сервера, все письма с JWT-токенами и кодами подтверждения будут создаваться в директории `sent_emails`. Для отправки запросов к API и получения ответов можно воспользоваться инструментом [Postman](https://www.postman.com/downloads/) или аналогичными сервисами; 
 
- На страницу администрирования можно войти по данным суперпользователя по адресу [localhost:8000/admin/](http://localhost:8000/admin/).