# Задача № 3.
#
# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

# Функция №1.генерация массива
def arrRandom():
    print('Генерирую массив из  50 чисел ... ')

    array = []
    for i in range(-25,25):
        rnd_elem = random.randint(-30, 30)
        array.append(rnd_elem)

    print(array)
    print(f'Исходная длинна массива: {len(array)}')
    return array

# Функция №2.
def rmv_doubble(create_arr):

    removeEl = list(set(create_arr))
    print(removeEl)
    print(f'Длинна массива после удаления дублей: {len(removeEl)}')

    calcPercentRemov = (len(create_arr)-len(removeEl))*100 / len(create_arr)
    print(f'Процент повторов значений: {calcPercentRemov} %')


# 1. вызов генератора массива
create_arr = arrRandom()

# 2. вызов ф-ции , где убирем повторы значений в массиве
rmv_doubble(create_arr)

