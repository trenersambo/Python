# =================================
# Задача
# сформировать строку из 10 символов
# на четных позициях д.б. четные цифры
# на нечтеных - буквы

# string = 'abcdefghjk'
# arr = list(string)
# print(arr)               # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k']
#
# for idx in range(len(arr)):
#
#     print(idx, arr[idx]) # индекс / значение (до замены)
#
#     if idx % 2 == 0:
#         arr[idx] = idx   # замена на четную цифру (на свой четный индекс)
#
# print(arr)



# ================================

# Задача

# Дана строка
# Покажи номера символов, совпадающих с последним символом строки

# string = 'aFRfrTfFsf'
# string = string.upper() # aFRfrTfFsf --> AFRFRTFFSF
#
# arrStr = list(string)  # ['A', 'F', 'R', 'F', 'R', 'T', 'F', 'F', 'S', 'F']
# print(arrStr)
#
# lastEl = arrStr[len(arrStr)-1] # F
#
# accEl = []
#
# for i in range( len(arrStr) ):
#     print(i, arrStr[i]) # индекс / значение
#
#     if arrStr[i] == lastEl:
#         accEl.append(i) # все совпадение скинул в массив
#
# print(f' Массив совпавших символов: {accEl}') # [1, 3, 6, 7, 9]
#
# s = ' '.join(map(str, accEl))
# print(f' Номера совпавших символов: {s}') # 1 3 6 7 9


# ================================

# Задача
# Дана строка.
# Если она начинается на 'abc' - то заменить их на 'www'
# Иначе добавить в конец строки 'zzz'

# def reName(string):
#     # приводим к одному регистру
#     string = string.lower()
#     print(string)
#
#     # если вначале строки есть 'abc'
#     if string.startswith('abc'):
#
#         # то замена 'abc' на 'www'
#         string = string.replace('abc', 'www')
#         print(string)
#
#     else:
#         # иначе - в конец строки дописать 'zzz'
#         string +='zzz'
#         print(string)
#
# # вызов функции
# reName('abc-Frontend')
# reName('Fr-ABC-ontend')



# ================================

# Задача
#  Дана строка.
# Если ее длина больше 10, то оставить в строке
# только первые 6 символов.
# Иначе - дополнить строку символами 'о' до длины = 12

# def strng(name):
#     print(f'Длина строки: {len(name)}')
#
#     #'Python is cool_' > 10 символов
#     if len(name) > 10:
#         # делаем СРЕЗ от [0] до [6]
#         name = name[0:6]
#         print(name, len(name))
#
#     else:
#         #'Python !' < 10 символов
#         while len(name)!=12:
#             # Дописываю "о"
#             name +='o'
#         print(name, len(name) )
#
#
# strng('Python!')
# strng('Python is cool_')


# ================================

# Задача
# Создать список, на четных местах в котором стоят единицы,
# а на нечетных местах -числа, равные остатку от деления своего номера на 5

# import random
#
# arr = [1 for i in range(0,10)]
# print(arr)
#
# for idx,elm in enumerate(arr):
#     print(idx, elm, sep=' || ' )
#
#     if idx%2 !=0:
#         rndElm = random.randint(-10,10)
#         arr[idx] = rndElm/5
#         print(arr[idx] )
#
# print(arr)

# на входе: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# на выходе (к примеру): [1, -1.2, 1, -0.4, 1, -1.6, 1, 0.2, 1, -0.2]


# ================================

# Задача
#  создать список, который одинаково читается как ПАЛИНДРОМ


# str = 'Мы все вместе дружно изучаем Python'
# splStr = str.split()
# print(splStr)       # ['Мы', 'все', 'вместе', 'дружно', 'изучаем', 'Python']
# print(type(splStr)) # <class 'list'>
#
# splStr.reverse()
# print(splStr )      # ['Python', 'изучаем', 'дружно', 'вместе', 'все', 'Мы']
#
# newStr = ' '.join(splStr)
# print(newStr)       # Python изучаем дружно вместе все Мы

# упрощенный вариант
# arrStr = list(str)
# arrStr.reverse()
# print(arrStr)

# ================================

# Задача

# Массив.
# Найти три последовательных элемента в массиве, сумма которых максимальна.

# arr = [1,2,3,4,5,6,7,-8,9,0]
#
# acc = 0     # аккумулятор получаемых значений
# summ = 0
#
#
# for idx, eli in enumerate(arr[0:-2:1] ):
#     #print(idx, arr[idx], eli) # Индекс, значение, значение
#
#     acc = arr[idx]+arr[idx+1]+arr[idx+2]
#     #print(acc)
#
#     if acc >=summ:
#         summ = acc
#
# print(f'Большая сумма: {summ}')

# ================================

# Задача

#Проверить , содержит ли данный массив из n чисел, все числа от 1 до n

arr = [7,3,0,8,99,10,2,6,88,1,4,66,59,5,9,0]

num = int(input('введи число (1 ...до 8):')) #  ввел 6

userArr = list(range(1,num+1))
print(userArr) # [1, 2, 3, 4, 5, 6]

arrSet = set(arr)
userArrSet = set(userArr) # {0, 1, 2, 3, 99, 4, 6, 7, 8, 66, 10, 5, 9, 88, 59}
print(arrSet, userArrSet) # {1, 2, 3, 4, 5}

print(arrSet > userArrSet) # True (для 1... 6) # False (для 10 и более)








