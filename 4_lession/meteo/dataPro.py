# МОДУЛЬ № 1: получение данных

from random import randint

# ф-ция Температуры (return рандомных значений)
def get_tempr(sens):
    return randint(-20, 0) if sens else randint(0, 20)

# ф-ция Атм.давления
def get_press(sens):
    if sens:
        return  randint(690, 750)
    else:
        return randint(750, 790)

# ф-ция СкорстьВетра
def get_speed(sens):
    if sens == 1:
        return randint(0, 20)
    else:
        return randint(20, 40)