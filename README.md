# Пульт охраны банка

Это внутренний репозиторий сотрудников банка "Рога и копыта".

Вы не сможете запустить сайт, так как у Вас нет доступа к базе данных, но Вы можете ознакомиться с моделью данных, со структурой сайта и запросами к базе данных.

Пульт охраны - это сайт, который подключается к базе данных с визитами и карточкам доступа сотрудников банка.

### Реализованы следующие запросы:

1. Получение списка активных пользователей.
2. Получения списка пользователей в хранилище на текущий момент и время их нахождения там.
3. Проверка на подозрительность посещения хранилища.


# Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:

```Python
pip install -r requirements.txt
```

### Переменные окружения

Для корректной работы модуля необходимы следующие переменные окружения:

```Python
DB_ENGINE='Ссылка на БД'
DB_HOST='Сервер базы данных'
DB_PORT='Порт сервера БД'
DB_NAME='Имя БД'
DB_USER='Имя пользователя БД'
DB_PASSWORD='Пароль пользователя БД'
```


### Пример запуска

```
python manage.py runserver
``` 
Starting development server at http://127.0.0.1:8000/


# Цель проекта

Код написан в образовательных целях на онлайн-курс для веб-разработчиков [Devman](https://dvmn.org/).