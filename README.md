# Курсовая работа 7.1 Django_DRF

**Контекст**

В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. 
Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер полезных привычек.
В рамках учебного курсового проекта реализуйте бэкенд-часть SPA веб-приложения.


**Описание**
Создание полезной привычки
Получение уведомлений Телеграм


**Технологии**

- Python
- Django
- DRF
- PostgreSQL
- Redis
- Celery

**Для работы с проектом необходимо.**  
- Клонировать репозиторий на компьютер используя SSH ключ.
- Создать зависимости, выполнив команду pip3 install -r requirements.txt
- В файл .env внесите свои данные (необходимые переменные перечислены в файле .env.sample)
- создайте и примените мигации (python manage.py makemigrations, python manage.py migrate)
- установите Redis, запустите командой redis-server
- для запуска проекта наберите в терминале команду python manage.py runserver
- в программе Postman зарегистрируйтесь и создайте привычки
- в терминале запустите celery worker командой:
  celery -A config worker -l INFO
- в другом терминале запустите celery beat командой:
  celery -A config beat -l info -S django
- зайдите в телеграм бот и нажмите START
