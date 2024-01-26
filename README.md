# Домашнее задание к лекции 1. «Import. Module. Package»

1. Структура программы «Бухгалтерия»:
- main.py;  
- application/salary.py;  
- application/db/people.py;
- application/star/star_svg.py

Main.py — основной модуль для запуска программы.  
В модуле salary.py функция calculate_salary.  
В модуле people.py функция get_employees. 
В модуле star_svg.py функция star

2. Функции импортируются в модуль main.py и оттуда вызываются.
* При импортировании функции calculate_salary выводится текущее время и дата
* При импортировании функции get_employees выводится текущее время и дата в Китае
* При импортировании функции star выводится сообщение "Импорт из модуля star_svg"

3. Инсталлирован пакет 'svg-turtle', позволяющий записывать в svg-файл рисунок в turtle. 
Создан файл [requirements.txt](requirements.txt), в котором указана его актуальная версия.
В модуле star_svg.py реализован функционал этого модуля -
рисуется звезда и записывается в файл [example.svg](example.svg).  


4. Функция calculate_salary выводит текст "Это запуск функции из модуля application.salary"
5. Функция get_employees выводит текст "Это запуск функции из модуля application.db.people"
6. Создан модуль dirty_main.py в котором импортированы все функции с помощью
конструкции 
```
from package.module import *
```
При запуске этого модуля, видно, что импортируются все функции из всех модулей, при том что запустить нужно только одну.

  


