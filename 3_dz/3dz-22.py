# print('дмашнее задание №1 к семинару 3')

# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



import random

# 1. ф-ция создания массива из- кол-ва указанных элементов
def getRandomList(num):
    num = int(num)
    print(num, type( num) )

    # создаю спиосок (массив) из указанного диапазона
    # range(-num, num, 2) -> (старт, финиш, шаг)
    randomList = [i for i in range(-num, num, 3)]

    #проверка наполняемости Списка, его тип <list>
    print(randomList, type(randomList))
    return  randomList

# 2.  ф-ция нахождения чисел на НЕЧЕТНОЙ позиции и их СУММА
def odd_summ(my_list):
    # accum сборщик итогов суммы
    accum = 0

    #операции над списком (итерация)
    for j in my_list:

        # проверка j должен = элементам Списка
        # randomList.index(j) - способ определения ИНДЕКСА в СПИСКЕ
        print(f'Для числа j = {j} --> Индекс:{my_list.index(j)} ')

        if ( my_list.index(j) % 2 > 0):

            # проверка числа на нечетной позиции и его тип (нужен int)
            print(f'Число {j} ({type(j)}) на НЕчетной позиции ')

            accum +=j
            print(f'сумма = {accum} \n')
    print(f'сумма элементов на Нечетных позициях = {accum} ')



num = input('Введи число (лучше больше 6): ')

# 1.вызов ф-ции создания массива из- кол-ва указанных элементов
my_list = getRandomList(num)

# 2. вызов ф-ции нахождения Чисел на нечетной позиции и их суммы
odd_summ(my_list)


