# Задача № 3.

# Задай список из n чисел последовтельности (1+1/n)^n
# Выведи на экран их сумму.
#
# Пример:
# Для n= 4 {1: 2, 2:2.25, 3: 2.34, 4: 2.44}
# Сумма: 9,06


def subsec(num):

    #num = float(num)
    # print(type(num), num) # <class 'int'> 4

    # сгенерировать ряд от 1 до ... num (от 1 до 4)
    arrLst = [i * 1 for i in range(1, num + 1)]
    #print(arrLst)  # [1, 2, 3, 4]


    # сборщик итогов
    accum = 0

    for j in arrLst:
        expr = (1+1/j)**j
        #print(expr, type(expr) ) # число и <class 'float'>

        accum += expr
        #print(accum, type(accum) ) # нараст. итог и <class 'float'>

    return round(accum, 3)

# вызов ф-ции:
print(subsec(4))


#====вариант 2 ==========

# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# #*Пример:*
#     - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

print('Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.')
n = int(input('Введите число N:-> '))
seq = dict()
seq_sum = 0
for i in range(1, n+1):
    seq[i] = round((1+1/i)**i, 2)
print(f'Для N={n} {seq}')
print(f'Сумма {sum(seq.values())}')
