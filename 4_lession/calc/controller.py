# Задача: связать между собой :
#  - файл № 1: ИНИЦИАЛИЗАТОР и
#  - модуль №2: типа UI

# создаем "кнопку" для юзера

# импорт файлов: model.py , view.py
import model
import view

def btn():

    # получены данные из файла view.py
    value_a = view.get_value()
    value_b = view.get_value()

    # инициализация входных данных через ф-л model.py
    model.init(value_a, value_b)

    # вычисление суммы (через ф-цию в файле model.py)
    result = model.mathem()

    # вывод результата (ф-ция печати из файла view.py)
    view.view_data(result, 'Итог:')






