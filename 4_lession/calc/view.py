# модуль №2: типа UI ( с чем взаимодействует юзер)
# модуль не привязан к логике


# пришли данные --> распечатать

def view_data(data, text):
    print(f'{text} = {data}')


# ввод данных (input)

def get_value():
    return int(input('value = '))