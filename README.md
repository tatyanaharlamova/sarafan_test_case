**ПРОЕКТ МАГАЗИНА ПРОДУКТОВ ИСПОЛЬЗОВАНИЕМ DRF.**

**Описание**
Приложение позволяет авторизованному пользователю осуществлять CRUD операции с категориями и подкатегориями, продуктами,
добавлять и удалять товары из корзины с подсчетом общего количества и стоимости.


**Технологии**

- Python
- Django
- DRF
- PostgreSQL

 
**Для работы с проектом необходимо.**  
- Клонировать репозиторий на компьютер используя SSH ключ.
- Установить зависимости из файла requirements.txt.
- В файл .env внесите свои данные (необходимые переменные перечислены в файле .env.sample)
- Примените мигации (python manage.py migrate)
- Для запуска проекта наберите в терминале команду python manage.py runserver
- Для доступа к административной странице нужно создать суперпользователя командой python manage.py csu


**Документация API**

Документация API доступна после запуска сервера по адресу: http://localhost:8000/redoc/ или http://localhost:8000/swagger/
