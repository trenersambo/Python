#===== seminar 2 15/12/2022

# пример РАНЖЕ

# range(5) -> range(start=0, stop=5, step=1):
# range(1,5) -> range(start=1, stop=5, step=1)
# range(1,9,2) -> range(start=1, stop=9, step=2)
# range(9,1,-1) -> range(start=9, stop=1, step=-1)

# =============================

## Групповая работа [2 семинар]

# 1. Напишите программу, которая принимает на вход число N и
# выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81


# 2. Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.
    
#     *Пример:*
    
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# 3. Напишите программу, в которой пользователь будет 
# задавать две строки, а программа - определять количество вхождений 
# одной строки в другой.


# ======== задача №1 ==========
# генератор списков
from itertools import count
import random # имп. модуля

num = int(input("Ведите число: "))

a=[random.randint(-10,10) for i in range( num)]
print (a)
# print (*a, sep='-')

    #.randint - рандом целочисленного
    #for i in range( num) - список 


# ======== задача №1 (для новичков)==========
import random

num = int(input("Ведите число: ")) #   = 5

a = []
for i in range(num):
    a.append(random.randint(-10,10) )

print(a)


# ======== задача №2  ==========

# 2. Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.
    
#     *Пример:*
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# ====== генератор словарей ==========

num = int(input("Ведите число: "))
d = {a: 3*a+1 for a in range(1, num+1)} # d - словарь
print (d)

# ======== задача №2 (вариант от Натальи) ==========

n = int(input('Print your N: '))
my_dict = {} # словарь
# my_list =[]  список
for i in range(1,n+1):
    my_dict[i] = 3*i + 1
print(my_dict)


# ======== задача №3  ==========

first_str = str(input('Введите исходную строку: '))
second_str = str(input('Введите строку: '))
count = 0
for i in range(len(first_str)-len(second_str)):
    if first_str[i] == second_str[0]:
        flag = True
        for j in range(1,len(second_str)):
             if second_str[j] != first_str[i+j]:
                 flag = False
        if flag:
            count += 1
print(count)

# ======== задача №3 (проще) ==========

sting1=input('Type text: ')
sting2=input('What you are looking for? ')

print(sting1.count(sting2))

