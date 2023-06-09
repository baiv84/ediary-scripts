# ПРЕАМБУЛА

Файл `scripts.py` представляет из себя набор функций для выполнения следующих операций над базой данных электронного дневника:

 * удаление `ВСЕХ` плохих оценок (двоек и троек) у  определенного ученика;
 * удаление `ВСЕХ` замечаний, сделанных учителями в адрес определенного ученика;
 * генерация `случайным образом выбранной` похвалы по указанному предмету обучения в адрес определенного ученика.


## Установка скрипта

* Прежде чем запускать скрипты, повышающих успеваемость ученика, у Вас должен иметься доступ к сайту электронного дневника школы;

* Перейти в рабочий каталог электронного дневника школы и скопировать в него файл `scripts.py`.

* Далее, активировать виртуальное окружение, содержащее все зависимости для запуска электронного дневника.

* На примере того, что виртуальное окружение проекта установлено в папку `venv`, команда по его активации будет иметь вид:

```code
    source venv/bin/activate
```

* Далее, необходимо запустить django shell, выполнив команду:

```code
    python manage.py shell
```

![Alt text](img/1.png?raw=true "Import script module")

* Находясь в режиме `django shell` - импортируйте модуль `scripts.py`, выполнив команду:

```code
    import scripts
```


Следующий шаг - находясь в режиме `django shell`, выполнить определенную процедуру по улучшению успеваемости ученика (см. следующий раздел - `Использование скрипта`)


## Использование скрипта

1. Исправление плохих оценок ученика, заданного по имени:

    ```code
        scripts.fix_marks(child_name='Гордеев Олимпий')
    ```

    ![Alt text](img/2.png?raw=true "Fix bad marks")

В случае отсутствия параметра `child_name` - действие будет произведено над оценками ученика: `Фролов Иван`

Функция возвращает в качестве результата количество исправленных оценок в базе данных.

В случае возникновения ошибки - возвращается значение: `-1`.


2. Удаление всех замечаний ученика, заданного по имени:

    ```code
        scripts.remove_chastisements(child_name='Гордеев Олимпий')
    ```

    ![Alt text](img/3.png?raw=true "Remove chastisements")

В случае отсутствия параметра `child_name` - действие будет произведено над замечаниями ученика: `Фролов Иван`

Функция возвращает в качестве результата количество удаленных замечаний пользователя из базы данных.

В случае возникновения ошибки - возвращается значение: `-1`.


3. Добавление случайно выбранной похвалы по заданному предмету для пользователя с определенным именем:

    ```code
        scripts.create_commendation(child_name='Гордеев Олимпий', subject_title='Музыка')
    ```

    ![Alt text](img/4.png?raw=true "Сreate commendation")

В случае отсутствия параметра `child_name` - похвала будет объявлена ученику: `Фролов Иван`

В случае отсутствия параметра `subject_title` - похвала будет объявлена по предмету: `Математика`

Функция возвращает в качестве результата - `значение кода операции`.

В случае возникновения ошибки - возвращается значение: `-1`.

При успешном добавлении похвалы  - возвращается значение: `0`.


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
