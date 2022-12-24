# Задача № 2.
#
# Задай натуральное число N
#
# Создать программу, которая составит список
# простых множителей числа N

# ================================

# ( натуральное число = от 1 до ...)
# ( простые множители числа N%2=0 ->  %3=0  %5=0 -> %7=0->... 11,13,17,19,23,29,31,37,41,43,47)

# ToDo:
# [+] список list из простых чисел
# [+] задать число N
# [+] Натуральн. число N проверить на делимость простыми числами

def multi(numList):
    numList = int(numList)
    #print(numList, type(numList))

    # создан список из чисел (от 1 до numList+1)
    numArr = [i for i in range(1, numList+1)]
    #print(numArr, type(numArr))


    # внутри спсика проверяем на ПРОСТОЕ ЧИСЛО:
    arrPrime = []
    for j in numArr:
        if j > 1:
            for n in range(2, j):
                if(j%n) == 0:
                    break
            else:
                #print(f'Простое число: {j}')
                arrPrime.append(j)

    #print(arrPrime) # Список собраных простых чисел

    return arrPrime

# 2. Ф-ция для вывода простых множителей числа N
def addListPrime(numMulti, num):
    num = int(num)
    print(f'На входе список из простых чисел {numMulti}, тип: {type( numMulti[0] )}\n'
          f'Интервал списка: от 1 до {num}, тип: {type(num)} ')

    #массив-аккумулятор для сбора списка простых множителей
    arrListPrime = []
    for i in numMulti:

        while(num % i == 0):
            num = num / i
            print(f'num={num} , i ={i} ')
            arrListPrime.append(i)
        else:
            continue

    # контроль: для числа 12376: [2, 2, 2, 7, 13, 17]
    print(f'Простые множители числа {num}: {arrListPrime}')


num = input('Введи число для проверки на простые множители: ')

# вызов ф-ции генерации простых чисел ( лимит - введенное юзером число )
numMulti = multi(num)

# вызов ф-ции создания списка простых множителей числа num
addListPrime(numMulti, num)


