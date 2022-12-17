# Задача № 3.

# Задай список из n чисел последовтельности (1+1/n)^n
# Выведи на экран их сумму.
#
# Пример:
# Для n= 4 {1: 2, 2:2.25, 3: 2.34, 4: 2.44}
# Сумма: 9,06


def subsec(num):

    #num = float(num)
    print(type(num), num) # <class 'int'> 4

    # сгенерировать ряд от 1 до ... num (от 1 до 4)
    arrLst = [i * 1 for i in range(1, num + 1)]
    print(arrLst)  # [1, 2, 3, 4]


    # сборщик итогов
    accum = 0

    for j in arrLst:
        expr = (1+1/j)**j
        #print(expr, type(expr) ) # число и <class 'float'>

        accum += expr
        #print(accum, type(accum) ) # нараст. итог и <class 'float'>








# вызов ф-ции:
subsec(4)