# 3. Задайте два числа.
# Напишите программу, которая найдёт НОК
# (наименьшее общее кратное) этих двух чисел.
 
# Пример НОК: 99 и 54; НОК (99, 54) = 594
# 99*54 = 5346
# 594 / 99 = 6
# 594 / 54 = 11

# ======== Решение задачи №3 (просто перебором всех чисел)=============

a = int(input('введи А: '))
b = int(input('введи B: '))

max_num = max(a,b)

for i in range(max_num, (a*b)+1, max_num): # ранж от .. до ПРЕДЕЛА
    if i % a == 0 and i % b == 0:
        print(f'НОК: {i}')
        break


 






