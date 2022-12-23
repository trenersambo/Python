import math #импорт модуля МАТЕМАТИКА
from decimal import Decimal #импорт модуля .... 

# №1. конвертация ввода в input() в вид "1.000...."
def calcLevel(d):

    #  отрисовка кол-ва нулей, которое введено в input()
    arr1 = [0 for i in range( int(d) )]
    #print(arr1, type(arr1[0])) # ---> [0, 0, 0, 0] <class 'int'>

    # перерисовка в вид "1.00000"
    numer = ''
    for i in arr1:
        numer +=str(i)
    numer = '1.'+numer
    #print(numer, type (numer))

    return numer

# №2. Вызов числа π и создание точности вывода его значения
def calcPi(numlevel):

    # присвоения числа π (инициализация)
    num = Decimal( math.pi)
    print(f'Число π (Без точности в кол-ве знаков): {num}')

    numOut = num.quantize( Decimal(numlevel) )
    print(f'Число π (C точностью до {len(numlevel)-2} знаков): {numOut}')



d = input("Укажите точность (кол-во знаков после запятой ) : ")
numlevel = calcLevel(d)

calcPi(numlevel)

