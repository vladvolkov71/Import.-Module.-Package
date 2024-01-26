from datetime import datetime as dt

print('Сейчас: ', dt.now())
print('Импорт из модуля ', __name__)


def calculate_salary():
    print('Это запуск функции из модуля ', __name__)
