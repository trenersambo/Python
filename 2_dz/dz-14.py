# Задача № 1.
# На вход вещественное число,
# На выходе сумма его цифр

# ===== Решение =======

def summ(num):                   # 1.5
    #print(num, type(num))        # 1.5 <class 'str'>

    if(',' in num):               # если в num есть ЗАПЯТАЯ
        num = num.replace(',', '')# замена ',' на пробел 1.5->15

    num = num.replace('.', '')   # замена '.' на пробел 1.5->15
    #print(num, type(num))        # 15 <class 'str'>

    lst_string = list(num)
    #print(lst_string, type(lst_string[0]))  # ['1', '5'] <class 'str'>

        # strIntg = map(int, lst_string)
        # print(strIntg, type(strIntg))

    accum = 0               # сборщик итоговых значений

    for i in lst_string:
        i = int(i)          # каждое значение <str> в -> <int>
        print(i, type(i))   # проверка
        accum +=i

    print(f'Сумма чисел = {accum}')

# без валидации на: минус, на буквы, на символы
num = input('введи положительное число : ')

# вызов ф-ции
summ(num)
