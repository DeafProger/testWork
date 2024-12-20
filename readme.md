Технические требования к тестовому заданию:

Python 3.8+

Django 3+

DRF 3.10+

PostgreSQL 10+

При выполнении тестового задания вы можете дополнительно использовать любые сторонние Python-библиотеки без всяких ограничений.


Само тестовое задание:

Создайте веб-приложение с API-интерфейсом и админ-панелью.

Создайте базу данных, используя миграции Django.


Требования к реализации:

Необходимо реализовать модель сети по продаже электроники. Сеть должна представлять собой иерархическую структуру из трех уровней:

 - завод;
 - розничная сеть;
 - индивидуальный предприниматель.

Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии). Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети, т. е. завод всегда находится на уровне 0, а если розничная сеть относится напрямую к заводу, минуя остальные звенья, ее уровень — 1.

Каждое звено сети должно обладать следующими элементами:
 - Название.
 - Контакты:
   - email,
   - страна,
   - город,
   - улица,
   - номер дома.
 - Продукты:
   - название,
   - модель,
   - дата выхода продукта на рынок.
 - Поставщик (предыдущий по иерархии объект сети).
 - Задолженность перед поставщиком в денежном выражении с точностью до копеек.
 - Время создания (заполняется автоматически при создании).

Сделать вывод в админ-панели созданных объектов.

На странице объекта сети добавить:

  - ссылку на «Поставщика»;
  - фильтр по названию города;
  - admin action, очищающий задолженность перед поставщиком у выбранных объектов.
  
Используя DRF, создать набор представлений:

CRUD для модели поставщика (запретить обновление через API поля «Задолженность перед поставщиком»).


Добавить возможность фильтрации объектов по определенной стране.

Настроить права доступа к API так, чтобы только активные сотрудники имели доступ к API.


КРАТКОЕ РУКОВОДСТВО ПО ИСПОЛЬЗОВАНИЮ:

#### Командой `git clone git@github.com:DeafProger/testWork.git` склонировать к себе репозиторий

#### Установить зависимости командой `pip install -r requirements.txt`

#### В файле .env.sample заполнить данные для работы с проектом и переименовать его в .env

#### Командами `python manage.py makemigrations` и `python manage.py migrate` инициализировать БД

#### Создать администратора БД командой `python manage.py createsuperuser`

#### Запустить через команду `python manage.py runserver` и зайти в админку для действий по управлению БД
