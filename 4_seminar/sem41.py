#

# 1 . Задайте строку из набора чисел.
# Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
#
# ==================================
#
# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0
# двумя способами:
#
#  - с помощью математических формул нахождения корней квадратного уравнения
#
#  - с помощью дополнительных библиотек Python
#
# ==================================
#
#
# 3. Задайте два числа.
# Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
#
#
# ===================================






# 1. Задайте строку из набора чисел.
# Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.



# ======== Решение задачи №1 (вар-т №1) =============

# list_num = input('Введите числа через пробел').split()
# print(list_num)
#
# list_num = list(map(int, list_num)) # переводим список строк в список чисел
# print(max(list_num), min(list_num)) # выводим максимальное и минимальное



# ======== Решение задачи №1 (вар-т №2) =============

# list_num = input('Введите числа через пробел: ').split()
# print(list_num)
#
# min_num = int(list_num[0])
# max_num = int(list_num[0])
#
# for num in list_num:
#     num = int(num)
#     if max_num < num:
#         max_num = num
#     if min_num > num:
#         min_num = num
# print(max_num , min_num)



# ======== Решение задачи №1 (вар-т №3) =============

def find_min_max(list_num):
    min_num = int(list_num[0])
    max_num = int(list_num[0])
    for num in list_num:
        num = int(num)
        if max_num < num:
            max_num = num
        if min_num > num:
            min_num = num
    return max_num, min_num

print('начало тела программы')
def main(): #тело программы
    list_num = input('Введите числа через пробел ->').split()
    print(*find_min_max(list_num))
print('конец тела программы')

if __name__ == "__main__":
	main()


