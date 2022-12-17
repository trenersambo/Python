# Задача № 4.

# На входе числа от -N до N.
# Дан список позиций, на которых расположены числа
#
# Найти произведениеэлментов на указанных позициях

# 1-я ф-ция: создаем массив из рандомных чисел (диапазон чисел: -N до +N)
def listUser(nPlus):
    # print(type (nPlus) ) # <class 'int'>

    nMinus = -nPlus
    # print(nMinus) #  -5 (если nPlus=5)

    # создать массив от -N до +N
    arr = [i*1 for i in range(nMinus, nPlus+1)]
    print(arr)  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

    return arr  #для передачи в функцию №2

# 2-я функция: сопостоваления:
def compare(arr, arrIdx):
    print(arr, arrIdx) # выдаст два массива, что переданы в параметрах

    arrValue = list()
    #print(arrValue)    #создание итерируемого СПИСКА (итирпа массив в JS)

    for i in arr:
        #print(f'Число из списка {i} => индекс: { arr.index(i) }') # так находят ИНДЕКС в Python

        for j in arrIdx:
            # print(f'Для i: {i} = j: {j}') #для -5 все цифры от 1до5, .. для -4 все от 1до5 ...
            # print(f'Для {arr[i]}: {arrIdx[j-1]}')

            if(arr.index(i)  == j):
                #print(f' Если {arr.index(i)} == {j}, то это число {i} ')
                arrValue.append(i)
    print(f'Массив для обработки: {arrValue}')

    return arrValue #для передачи в функцию №3


#3-я ф-ция: найти произведение найденных значений
def multi(compareArr):
    accumMulti = 1      #сборщик итогов

    for i in compareArr:
        accumMulti *= i

    print(f'произведение значений массива {compareArr} = {accumMulti}')   # 240 = (-4 * -3 * 4 * 5)

# 1. вызвал ф-цию наполнения массива 10-тью элементами, диапозон: -5 до +5
newArr = listUser(5)

# 2. вызвал ф-ию сравнения рандомного массива и [....](типа из файла file.txt (по ТЗ))
compareArr = compare(newArr, [1,2,10,9])

# 3. вызов ф-ции получения произвдения найденных значений после сравнения
multi(compareArr)