# МОДУЛЬ № 2: логирование

# импорт модуля ДАТА/ВРЕМЯ
from datetime import datetime as dt

# ф-ция логирования Температуры
#
def tempr_logger(data):
    # получение даты
    time = dt.now().strftime('%D:%H:%M:%S')

    # w - создать файл + запись с чистого листа
    # a - создать / продолжить запись в файл
    # r - чтение
    with open('log.csv', 'a') as file:

        # file - алиас
        # для разделения в csv по столбцам => ...; ... ;
        file.write(f'{time}; temperature;{data}\n')


def press_logger(data):

    time = dt.now().strftime('%M:%S')

    with open('log.csv', 'a') as file:

        file.write(f'{time}; pressure ;{data}\n')

def speed_logger(data):

    time = dt.now().strftime('%M:%S')

    with open('log.csv', 'a') as file:

        file.write(f'{time}; speed_wind ;{data}\n')

# NB! запуск ф-ции - ДЛЯ ПРИМЕРА работы
# tempr_logger(580)