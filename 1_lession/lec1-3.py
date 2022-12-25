# help(int) # вызов помощи по элементу (int); выход клавиша q

import math
print(math.cos(90))


print('hello world')

# ==== лекция №1 ==============

# ТИПЫ ДАННЫХ
# int
# float
# boolean
# str
# None
# 
#
# list
#... ... ... etc

#=============
#=============Пример 1 Присвоение переменных int, float , None, 'строка ', boolean
a  = 678
b = 1.888
print(a, b) # 678 1.888


c = None
print(c) #None

c = None
c = 987
print(c) #987

d = None

e = "Enot Rules'ed " + '4Ever'
print(e) # Enot Rules'ed 4Ever 

f = True
print(f) #True /  ... False


#=============
#=============Пример 2 Узнать тип: type()

print (type(a), type(b) ) # <class 'int'> <class 'float'> <class 'NoneType'>
print ( type(d) ) #   <class 'NoneType'>
print ( type(e) ) #   <class 'str'>



#=============
#=============Пример 3 СПИСКИ (вместо массивов)

list = [1, 2.65, 'строка' , False]
print(list) #[1, 2.65, 'строка', False]

col = ['unexpected indent', 'следи за пробелами!']








