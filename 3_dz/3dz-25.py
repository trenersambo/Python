# print('дмашнее задание №4 к семинару 3')

# Задача 25: Напишите программу, которая будет п
# реобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# 1024-512-256-128-64-32-16-8-4-2-1
            # 45 ---> 32-16-8-4-2-1
            #         1  0  1 1 0 1

# Перевод в двоичное (через остаток %)
# 45%2=1, 22%2=0, 11%2=1, 5%2=1, 2%2=0, 1%2=1

def DecToBin(dec):
    accum = ''              # сборщик итога
    while dec > 0:
        if dec % 2 == 1:    # Если остаток от % не 0
            accum += '1'    # то в итог пишу 1
        else:
            accum += '0'    # если остаток от % = 0, пишу 0
        dec //= 2           # получение целого числа

    return accum[::-1]      # разворот строки


decBin = int(input("Введите число для конвертации: "))
print(DecToBin(decBin))


