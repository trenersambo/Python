# print('дмашнее задание №5 к семинару 3')

# 5 Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
#
# *Пример:*
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# Фибоначчи:    0,1  0,1,1  0,1,1,2   0,1,1,2,3    0,1,1,2,3,5   0,1,1,2,3,5,8   0,1,1,2,3,5,8,13   0,1,1,2,3,5,8,13,21
# число юзера:   1      2       3       4               5               6               7                   8
# для положительных: F n = F n − 1 + F n − 2
# для отрицательных: f(n)= f(n+2) - f(n+1)

def calcFibi(num):
    #if для отрицательного числа (crutch)
    if (num < -1):
        num = -num

    arr = [0,1]     # стратовый массив; (по умолч.) при вводе 1 = [0,1]

    count = 1

    while(count<num):
        if num == 1:    #исключение для введенной 1
            print(arr)
            break

        if num > 1:
            acc = arr[len(arr)-1] + arr[len(arr)-2]
            arr.append(acc)

            count +=1

    print(f'Числа Фибоначчи для {num} = {arr}')
    return  arr


# 2. ф-ция для обработки массива с числами Фибоначчи для Отрицательных чисел
def calcFibiNeg(negNum):
    #if для отрицательного числа (crutch)
    if (negNum > -1):
        negNum = -negNum

    arrNeg = [0,1]  # стратовое знач. для негаФибоначчи: при вводе -1 = [0,1]

    count = -1

    while(count > negNum):
        #print(f'count={count} , negNum={negNum}')
        if negNum == -1:
            print(arrNeg)    #исключение для введенной -1 --> [0,1]

        if(negNum < -1):

            acc = arrNeg[len(arrNeg)-2] - arrNeg[len(arrNeg)-1]
            arrNeg.append(acc)

            count -=1   # -2 -3 -4 -5 ... пока не достигнет negNum

    print(f'Числа Фибоначчи для {negNum} = {arrNeg}')


# вызов методов/функций
numFibi = int(input('введи цифру для расчета числа Фибоначчи (>=1): '))
calcFibi(numFibi)

calcFibiNeg(numFibi)