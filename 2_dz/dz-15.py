# Задача № 2.
# на входе число N.
# На выходе - набор произведений чисел от 1 до N


def sumMulti(num):

    num = int(num)
    print(num, type(num))    # 4 <class 'int'>

    arrLst = [i*1 for i in range(1, num+1)]
    print(arrLst)            # [1, 2, 3, 4]

    accum = 1                # сборщик итога
    arrLstNum = []
    for j in arrLst:
        accum *=j
        print(accum)         # 1  2  6  24
        arrLstNum.append(accum)

    print(f'Набор произвдений от 1 до {num} = {arrLstNum} ')    # для 4: [1, 2, 6, 24]



num = input('введи целое число : ')

# минимальная валидация
if int(num)<1:
    print('введи число больше 1')


# вызов ф-ции:
sumMulti(num)