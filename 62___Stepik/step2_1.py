# Звездный треугольник (ver 1)

# for i in range(1,8):
#     print('*'*i)

# Звездный треугольник (ver 2 list comprechension)

# print(*list('*'*i for i in range(1,8)), sep='\n')

# 2.1 Часть 1 # 1 из 10 шагов пройден
# На easy

def calc(arrnum):
    a, b = arrnum

    # сумма чисел
    print(a + b)

    # разность чисел
    print(a - b)

    # произвдение чисел
    print(a * b)

    # частное чисел
    print(a / b)

    # цел часть от деления
    print(a // b)

    # остаток от деления
    print(a % b)

    # корень квадратный из суммы их 10-ых степеней
    print((a ** 10 + b ** 10) ** 0.5)


# arrnum = [int(input()) for i in range(2)]
# calc(arrnum)

# ////////////////////////////////////
# 2.1 Часть 1 # 2 из 10 шагов пройдено

def indexMassBody(arrData):
    mas, higth = arrData
    mas = float(mas)
    higth = float(higth)

    imt = mas / (higth * higth)

    if 18.5 <= imt <= 25:
        print('Оптимальная масса')
    elif imt < 18.5:
        print('Недостаточная масса')
    else:
        print('Избыточная масса')


# arrData = (input() for i in range(2))
# indexMassBody(arrData)


# ////////////////////////////////////
# 2.1 Часть 1 # 3 из 10 шагов пройдено
# Стоимость строки

def calculate(arr):
    total = len(arr) * 60

    print(f'{total // 100} р. {total % 100} коп.')


# arr = list(input())
# calculate(arr)


# ////////////////////////////////////
# 2.1 Часть 1 # 4 из 10 шагов пройдено

# Количество слов

# ver 001
# arr = (input().split(' '))
#
# t = 0
# for i in range(len(arr)):
#     if arr[i].isalnum():
#         t += 1
# print(t)


# ver 002
# t = 0
# for i,el in enumerate( (input().split(' '))):
#     if el.isalnum():
#         t +=1
# print(t)


# ver 003
# print (sum(list( 1 for i,el in enumerate( (input().split(' ')))  if el.isalnum()  )))


# ver 004 (самое короткое! )
# print(len(input().split()))


# ////////////////////////////////////
# 2.1 Часть 1 # 5 из 10 шагов пройдено

# Зодиак

def showHoroscope(year):
    dic = \
        {
            0: 'Обезьяна', 1: 'Петух', 2: 'Собака',
            3: 'Свинья', 4: 'Крыса', 5: 'Бык',
            6: 'Тигр', 7: 'Заяц', 8: 'Дракон',
            9: 'Змея', 10: 'Лошадь', 11: 'Овца'
        }

    for i in dic.keys():

        if year % 12 == i:
            print(dic[i])


# year = int(input())
# showHoroscope(year)


# ////////////////////////////////////
# 2.1 Часть 1 # 6 из 10 шагов пройдено

# Переворот числа

def reverseNum(num):

    if len(num) == 5:
        d = num[5::-1]      # полный реверс строки
        d = d.lstrip('0')   # убрать нули слева
        print(d)
    elif len(num) == 6:
        print(num[0] + num[6:0:-1])

num = input()               # string !
reverseNum(num)
