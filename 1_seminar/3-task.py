
# 3. Напишите программу, которая принимает на вход число и
# проверяет, кратно ли оно 5 и 10 или 15, но не 30.

u_num = int(input('введи число: '))

if (u_num % 5 == 0 and u_num % 10 == 0 or u_num % 15 == 0) and u_num % 30 != 0:
    print('Твое число - норм!')
else:
    print('Придумай другое число')


# решение задачи №3 (для дробных чисел )

num = float(input('введи число: '))

if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
    print('Твое число - норм!')
else:
    print('Придумай другое число')