# Файл / МОДУЛЬ № 3

# импорт модулей №1 ПолученияДанных и №2 Логер
import dataPro as prov
import logger as log

def tempr_view(sensor):

    # получение данных о Температуре
    data = prov.get_tempr(sensor)

    # логирование данных о Температуре
     log.tempr_logger(data)

    return data


def press_view(sensor):
    data = prov.get_press(sensor)
    log.press_logger(data)
    return data


def speed_view(sensor):
    data = prov.get_speed(sensor)
    log.speed_logger(data)
    return data



