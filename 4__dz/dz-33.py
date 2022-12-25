# Задача № 4.
# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
#
# *Пример:*
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0



import random

#1. Ф-ция генерации списка коэфф-ов
def randomList(k):

    arr = [] # сборщик значений коэфф-ов мн.члена

    for i in range(0, k+1):
        rnd_el = random.randint(0,101)
        #print(rnd_el)
        arr.append(rnd_el)
    #print(f'Список коэфф-ов: {arr}')

    return arr  #Массив списка коэфф-ов многочлена



# 2. Ф-ция генерации многочлена степени k
def polynomial(valueArr):

    #print(f'Список коэфф-ов: {valueArr}')

    acc = ''

    for i in valueArr:
          idx = valueArr.index(i) # ИНДЕКС каждого значения из массива
          #print(idx+1)            # степени для (5): 1 2 3 4 5

          # создаю формулу многочлена
          acc += (f'{i}*{"x"}**{idx}')

          # ставлю знак "+" между значениями по условию (иначе лишний плюс будет)
          if idx < len(valueArr)-1:
              acc +=' + '



    acc += " = 0"
    print( acc)





k = int(input('укажи степень многочлена : '))

valueArr = randomList(k)

polynomial(valueArr)