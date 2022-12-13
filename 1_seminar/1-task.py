# Задачи:

# 1. Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.
    
#     *Примеры:* 
    
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет
# 2. Напишите программу, которая на вход принимает 5 чисел и 
# находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# ======================================

# Задача 1

num1 = int(input(' введите число1: ')) # вводим цифру
num2 = int( input(' введите число2: '))
print(f'Является ли {num1} квадратом {num2} :', end=' ') # end не дает делать перенос

if num1 ** 2 == num2 or num2 ** 2 == num1: # сравниваем первое=квадрату второго ? и наоборот
    print('да')
else:
    print('нет')

# Задача №2

num10 = int( input(' введите число1: ')) # вводим цифру
num20 = int( input(' введите число2: '))
num30 = int( input(' введите число3: ')) 
num40 = int( input(' введите число4: '))
num50 = int( input(' введите число5: '))
 
if num10 > num20 and num10 > num30 and num10 > num40 and num10 > num50:
    print(f'{num10} - максимальное число')
elif num20 > num10 and num20 > num30 and num20 > num40 and num20 > num50:
    print(f'{num20} - максимальное число')
elif num30 > num10 and num30 > num20 and num30 > num40 and num30 > num50:
    print(f'{num30} - максимальное число')
elif num40 > num10 and num40 > num20 and num40 > num30 and num40 > num50:
    print(f'{num40} - максимальное число')
else:
    print(f'{num50} максимальное')


# Задача №2 (вариант 001)

num = []
for i in range(5):
    num.append(int(input(f'Введите цифру под номером {i}: ')))
print(num)
print(max(num))


# Задача №2 (вариант 002, с готовым массивом)

numbers = [1, 4, 6, 2, 3]
# for i in range(1,6):
#     numbers.append(int(input(f'Введите элемент под номером {i}: ')))
print(numbers)
print(max(numbers)) 

# Задача №2 (вариант 003, решение сеньоров)

my_max = 0
for _ in range(5):
    num = int(input('Введите число: '))
    if my_max < num:
        my_max = num

print(my_max)

