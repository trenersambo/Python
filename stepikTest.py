# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint

# задаем требуюмую степень многочлена
k = 3

# функция герерирования случайного многочлена степени n с коэффициентами в диапазоне от 0 до 99
def generate_polystring(n):
    generated_poly = ""
    # идем от n до 0
    for i in range(n, -1, -1):
        # вычисляем рандомный коэффициент от 0 до 99
        rnd = randint(0,100)
        # если коэффициент степени текущей итерации не 0, то добавляем его
        if rnd != 0:
            # если элемент не первый, то добавляем в строку +
            if len(generated_poly) > 1:
                generated_poly += " + "
            # если итерация последняя, то добавляем коэффициент без x**, т.к. x**0 == 1
            if i == 0:
                generated_poly += str(rnd)
            else:
                generated_poly += str(rnd) + "*x**" + str(i)
    # в конце строки добавляем = 0
    generated_poly += " = 0"
    return generated_poly

def main():
    # генерируем строку с многочленом
    polynom = generate_polystring(k)
    # печатаем его
    print("Случайный многочлен:", polynom)
    # записываем в файл polynom5.txt, например
    with open("polynom5.txt", "w") as file1:
        file1.write(polynom)

if __name__ == "__main__":
    main()
