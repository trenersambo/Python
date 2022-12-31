# def addArr(a ):
#
#     arr = []
#     for i in list(a):
#         arr.append( int(i) )
#     return arr
#
#
#
#
#
# def calc(caclEl):
#
#     a,b,c = caclEl
#     # print(a,b,c,type(a) )
#
#
#     print(f'{a}{b}{c}\n'
#           f'{a}{c}{b}\n'
#           f'{b}{a}{c}\n'
#           f'{b}{c}{a}\n'
#           f'{c}{a}{b}\n'
#           f'{c}{b}{a}')
#
#
# a = input()
# caclEl = addArr(a)
#
# calc(caclEl)


# ===================

# put your python code here
# def calc(num):
#
#    arrEl = list(num)
#
#    a,b,c,d = arrEl
#
#    print(f'Цифра в позиции тысяч равна {a}\n'
#          f'Цифра в позиции сотен равна {b}\n'
#          f'Цифра в позиции десятков равна {c}\n'
#          f'Цифра в позиции единиц равна {d}')
#
# num = input()
# calc(num)

# ТЫСЯЧИ СОТНИ ДЕСЯТКИ ЕДИНИЦЫ
# num//1000   # thousands
# num//100%10 # hundreds
# num%100//10 # dozens
# num%10      # units

# ===================

# print('*****************')
# print('*               *')
# print('*               *')
# print('*****************')

# ===================
# import math
# def calc(a,b):
#
#     print(f'Квадрат суммы {a} и {b} равен {int(math.pow((a+b), 2))}')
#     print(f'Сумма квадратов {a} и {b} равна {a**2 + b**2}')
#
# a = int(input())
# b = int(input())
#
# calc(a,b)


# ===================

# def calc(a,b,c,d):
#
#     arr = [a,b,c,d]
#     a, b, c, d = arr
#
#     summ = a**b + c**d
#     print(summ)
#
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# calc(a,b,c,d)



# ===================

# a = input()
#
# n   = [a for i in range(1,4,3)]
# n1 = int(n[0])
# # print(n1)
#
# nn  = [a for i in range(1,4,2)]
# nn1 = int(nn[0]+nn[1])
# # print(nn1)
#
#
# nnn = [a for i in range(1,4,1)]
# nnn1 = int(nnn[0]+nnn[1]+nnn[2])
# # print(nnn1)
# #
# # print(n, nn, nnn)
#
# print(n1+nn1+nnn1)



# =================== экзамен закончился

# i = int(input('Введи число: '))

# if i / 2:
#     print(i, 'чётное')
# else:
#     print(i, 'нечётное')

# if i // 2:
#     print(i, 'чётное')
# else:
#     print(i, 'нечётное')

#3 - ok
# if i % 2 == 0:
#     print(i, 'чётное')
# else:
#     print(i, 'нечётное')

# if i // 2 == 0:
#     print(i, 'чётное')
# else:
#     print(i, 'нечётное')

#5 - ok (перестановка сбила с толку :-) )
# if i % 2 != 0:
#     print(i, 'нечётное')
# else:
#     print(i, 'чётное')

# if i // 2 != 0:
#     print(i, 'нечётное')
# else:
#     print(i, 'чётное')

# def compare(pswd1, pswd2):
#     if pswd1 == pswd2:
#         print('Пароль принят')
#     else:
#         print('Пароль не принят')
#
# pswd1 = input()
# pswd2 = input()
#
# compare(pswd1, pswd2)

# i = int(input())
# if i % 2 != 0:
#      print('нечётное')
# else:
#      print('чётное')
#
# print(('Четное','Нечетное')[ int(input()) % 2 ])

# ТЫСЯЧИ СОТНИ ДЕСЯТКИ ЕДИНИЦЫ
# num//1000   # thousands
# num//100%10 # hundreds
# num%100//10 # dozens
# num%10      # units

# def compare(num):
#     arr = list(num)
#     a,b,c,d = arr
#
#     if int(a) + int(d) == int(b) - int(c):
#         print('ДА')
#     else:
#         print('НЕТ')
#
# num = input()
# compare(num)

#print(('Доступ разрешен','Доступ запрещен')[ int(input()) < 18 ])

# Арифметическая прогрессия  - это числовая последовательность  , в которой каждое число, начиная со второго,
# получается из предыдущего добавлением к нему постоянного числа (так называемого шага).
# Соответственно третье число арифметической прогрессии будет равно - разности второго и первого числа
# прибавленного к второму числу:
#
# допустим, есть последовательность  трех чисел:  a b c
#
#  a - первое число,
# b - второе число,
# c - третье число,
# ( b - a) - шаг , чтобы понять является ли данная последовательность  арифметической прогрессией,
# должно выполнятся условие: \
#
#     ( b - a) + b = c
#  или: b-a = c-b



# def calc(a,b,c):
#
#     arr = [a,b,c]
#     a, b, c = arr
#
#     if b-a == c-b:
#         print('YES')
#     else:
#         print('NO')
#
# a = int(input())
# b = int(input())
# c = int(input())
#
#
# calc(a,b,c)

# =====================

# 4.1.3.  Напишите программу, которая определяет наименьшее из двух чисел.
#
# Решение 1
#
# def minEl(a,b):
#
#     arr = [a,b]
#     minEl = min(arr)
#     print(minEl)
#
# a = int(input())
# b = int(input())
#
# minEl(a,b)
#
#
# Решение 2
#
# n = [int(input()) for _ in range(2)]
# print(min(n))
#
# Решение 3
# print(min(int(input()), int(input())))

# =====================

# 4.1. Напишите программу, которая определяет наименьшее из четырёх чисел.

# def minEl(a,b,c,d):
#
#     arr = [a,b,c,d]
#     min_elm = arr[0]
#
#     for i in arr:
#         if i <= min_elm:
#             min_elm = i
#
#     print(min_elm)
#
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# minEl(a,b,c,d)

# Решение 2
# sp = []
# for i in range(4):
#     a = int(input())
#     sp.append(a)
# print(min(sp))



# print(min(int(input()), int(input()), int(input()), int(input())))

# =====================

# Задача stepik № 4.1.4
#
# Напишите программу, которая по введённому возрасту пользователя сообщает,
# к какой возрастной группе он относится:
#
# до 13 включительно – детство;
# от 14 до 24 – молодость;
# от 25 до 59 – зрелость;
# от 60 – старость.

# def age(num):
#
#     if num >= 60:
#         print('старость')
#     if (25 <= num <= 59):
#         print('зрелость')
#     if (14 <= num <= 24):
#         print('молодость')
#     if (0 <= num <= 13):
#             print('детство')
#
# num = int(input())
# age(num)


# Решение 2
# n = int(input())
# print("старость" if n>59 else "зрелость" if n>24 else "молодость" if n>13 else "детство")

# Решение 3

# a = int(input())
# print(['детство', 'молодость', 'зрелость', 'старость'][sorted([13, 24, 60, a]).index(a)])


# 4.1...
# Напишите программу, которая считывает три числа
# и подсчитывает сумму только положительных чисел.

def addCalc(a,b,c):

    arr = [a,b,c]

    acc_sum = []

    for i in arr:
        if i<0:
            i=0
        acc_sum.append(i)

    summ = sum(acc_sum)
    print(summ)



a = int(input())
b = int(input())
c = int(input())

addCalc(a,b,c)


