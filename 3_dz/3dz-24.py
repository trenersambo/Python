# print('дмашнее задание №3 к семинару 3')
def floatNum(arr):

    #Поиск выделения ДЕСЯТИЧНОЙ ЧАСТИ:
    # a = 100.531
    # round(a%1 , 3) --> 0.531

    arrDecimal = []
    for i in arr:

        #  выделение значения после точки (помещаю в отд. массив):
        # if нужен для валидной отработки чисел > 0  и < 0
        if i > 0:
            decimal = round(i%1 , 3)
        else:
            decimal = round(i % (-1), 3)

        #ПРОПУСК размещения НУЛЯ в массиве
        if decimal == 0:
            continue
        #размещение в массив полученных значений
        arrDecimal.append(decimal)


    print(f'Дробная часть чисел на входе: {arrDecimal}')   #[0.1, 0.2, 0.1, 0, 0.01]

    # макс и миним. можно найти методами max(), min() !!
    maxEl = max(arrDecimal)
    minEl = min(arrDecimal)

    print(f'Разница {maxEl} и {minEl} = {round(maxEl - minEl , 3)}')

# вызов функции
floatNum([1.1, 1.2, 3.1, 5, 10.01])
