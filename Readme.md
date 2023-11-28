# **Запуск проекта**
1. Создать виртуальное окружение `python3 -m venv venv`
2. Активировать виртуальное окружение
3. Установить необходимые пакеты командой `pip install -r requirements.txt`
4. Создать базу данных с именем candlewax, ввести необходимые изменения settings.py для подключения к базе данных
5. Запустить проект `python3 manage.py runserver`
6. Применить миграции `python3 manage.py migrate`
7. Применить команду `python3 manage.py fill` для заполнения базы данных


# **Задание 1**

**Создайте новый контроллер и шаблон, которые будут отвечать за отображение отдельной страницы с товаром. На странице с товаром необходимо вывести всю информацию о товаре.**

1. [x] выполнено


# **Задание 2**

**В созданный ранее шаблон для главной страницы выведите список товаров в цикле. Для единообразия выводимых карточек отображаемое описание обрежьте после первых выведенных 100 символов.**

1. [x] выполнено

# **Задание 3**

**Из-за расширения количества шаблонов появляется слишком много повторяющегося кода, поэтому выделите общий (базовый) шаблон и также подшаблон с главным меню.**

1. [x] выполнено

# **Задание 4**

**Для выводимого изображения на странице реализуйте шаблонный фильтр, который преобразует переданный путь в полный путь для доступа к медиафайлу:**</br>
`<!-- Исходный вариант -->`</br>
`<img src="/media/{{ object.image }}" />`</br>
`<!-- Итоговый вариант -->`</br>
`<img src="{{ object.image|mediapath }}" />`
1. [x] выполнено

**Реализуйте описанный функционал с помощью шаблонного тега:**</br>
`<!-- Исходный вариант -->`</br>
`<img src="/media/{{ object.image }}" />`</br>
`<!-- Итоговый вариант -->`</br>
`<img src="{% mediapath object.image %}" />`
2. [x] выполнено


# **Задание 6**

1. [x] Через инструмент shell заполните список категорий, а также выберите список категорий, применив произвольные рассмотренные фильтры. В качестве решения приложите скриншот.
2. [x] Сформируйте фикстуры для заполнения базы данных.
3. [ ] Напишите кастомную команду, которая умеет заполнять данные в базу данных, при этом предварительно зачищать ее от старых данных.


# *** Дополнительное задание**

1. [ ] Добавьте функционал создания продукта через внешний интерфейс, не используя стандартную админку.
2. [ ] Реализуйте постраничный вывод списка продуктов.