from datetime import datetime, timedelta

print('Сейчас в Китае: ', datetime.now()+timedelta(hours=5))
print('Импорт из модуля ', __name__)


def get_employees():
    print('Это запуск функции из модуля ', __name__)
