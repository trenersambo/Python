# ======== Решение задачи №2 =============
# 2. Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.


list1 = ['2' , '3' , '4' , '5']
x = (input("Введите число: "))

for i in list1:
    if x == i:
        print(f'да, есть число {i} в списке')
        break
else:
    print("нет числа в списке")

# ======== Решение задачи №2 (вариант 001)=============

def check(stringlist: list, n: str) -> bool:
    for i in stringlist:
        if n == i:
            return True
    return False

my_list = ["2", "3", "3425", "0", "-1"]
x = input("Введите искомое число: ")
if check(my_list, x):
    print("Число есть в последовательности", my_list)
else:
    print("Числа нет в последовательности", my_list)

