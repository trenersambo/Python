#=============
#=============Пример 7 Логические операции

# > , >=, < , <= , == , !=

# not , and , or (не путай с & , | , ^)

# is, is not , in , not in

numLogic = 10 < 40 and 50 > 25
# print(numLogic)   # True

str1 = 'string'
str2 = 'string'
# print( str1 == str2 )   # True


arr1 = [1 , 5]
arr2 = [1 , 5]
# print(arr1 == arr2 )   # True # сравнение поэлементное


numb1 = 10
numb2 = 40
numb3 = 500
print( numb1 < numb2 < numb3 )  # True

print( 1 > 2 or 4 < 10)         # True (т.к. дизюнкция одного из высказываний в or = истина)

arr3 = [1,2,3,4]
print(4 in arr3)                # True ( 4 есть в Списке arr3)





#=============
#=============Пример 8 Управляющие конструкции IF IF-ELSE

# Задача 8.1. Найти максимум из двух чисел

intNum1 = int( input('Первое число: ') )
intNum2 = int( input('Второе число: ') )

if intNum1 > intNum2:
  print(intNum1)
else:
  print(intNum2)


#=============
#=============Пример 8.1. Управляющие конструкции IF ELIF

sport = input("Твой спорт:")
if sport == "sambo":
  print(f'{sport} - это норма жизни ')
elif sport == 'judo':
  print(f'{sport} - это стиль ')
elif sport == 'bjj':
  print(f' и {sport} как движуха ')
else:
  print(f'{sport} ?  нормально так')


#=============
#=============Пример 8.2. Управляющая конструкция WHILE

# Задача 8.2.1 Перевернуть число (25 ---> 52)
orig = 25
reversOrig = 0

while orig !=0:
  reversOrig = reversOrig*10 + (orig % 10)
  orig = orig // 10
print(reversOrig)


#=============
#=============Пример 8.3. Управляющие конструкции WHILE-ELSE
# ELSE включается, когда основное тело цикла перестает работать 

# Задача 8.3.1 После окончания действия тела цикла, вывести сообщение
while orig !=0:
  reversOrig = reversOrig*10 + (orig % 10)
  orig = orig // 10
else:
  print('Переменная orig уже равна 0')
print(f'Реверсированное число: {reversOrig}')


#=============
#=============Пример 8.4. Управляющая конструкция FOR IN

# Задача 8.4.1 Вывести на экран квадрат каждого значения

for i in 1,2,3,4:
    print(f'{i} в квадрате: {i**2}') # 1 4 9 16

arrSqw = [10,20,30]
for i in arrSqw:
    print(f'{i} в квадрате: {i**2}') # 100 400 900


# Задача 8.4.2 Использование range()

intRang = range(10)
for i in intRang:
    print(f'{i+1}-е число: {i}') # покажет числа от 0....9


# Задача 8.4.3 Использование range() для вывода нечетных чисел

for i in range(1 , 9, 2):        # от 1 до 8, с шагом 2
    print(f'{i+1}-е число: {i}') # 2-е число: 1 , 4-е число: 3, 6-е число: 5, 8-е число: 7


# Задача 8.4.4 Разбить слово 'sambo' по буквам

for i in 'sambo':        
    print(i)    #  s   a   m   b   o


#=============
#=============Пример 8.5. про СТРОКИ

txt = 'Съешь еще этих мягих французких булок'
print( len(txt) )                   # 39 , кол-во символов
print( 'булок' in txt)              # True
print( txt.isdigit() )              # False
print( txt.islower() )              # True
print( txt.replace('eще' , 'уже') ) # замена

print( txt[0] )             # C
print( txt[len(txt)-1] )    # к
print( txt[len(txt)-2] )    # о
print( txt[-5] )            # б
print( txt[:] )             # ([0:]) весь текст
print( txt[0:2] )           # (от 0 до 2-го элемента) Cъ
print( txt[2:9] )           # (от 2 до 9 элемента) ешь еще
print( txt[6:-18] )         # (от 6 до -18 элемента) еще этих мяги
print( txt[0:len(txt):6])   # или [::6] Сеиинхк .... 


#=============
#=============Пример 9 СПИСКИ (массивы в JS C#)

# Список - пронумерованная , изменяемая коллекция объектов (любых??? типов)


#Задача 9.1. Каждое значение списка list умножить на 2

numbers = [1, 2, 3, 4, 5]
# print(numbers)      # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))       #Ошибка??: object is not callable
# print(numbers)      # [1, 2, 3, 4, 5]

numbers[0] = 10
print(numbers)        # [10, 2, 3, 4, 5]   # вместо 1 стала 10

for i in numbers:     # перебор для: 10  2  3  4  5
    i = i*2           # сам список list НЕ изменится

print(i)              # [20, 4, 6, 8, 10]
print(numbers)        # [10, 2, 3, 4, 5]   # Список (массив) не измене после for in



#Задача 9.2. Добавить (append) элемент в список list и удалить (remove, del) элемент

colorsArr = ['red' , 'green' , 'black']

colorsArr.append('gray')  #добавление в конец списка
print (colorsArr)         #['red', 'green', 'black', 'gray']

colorsArr.remove('red')   # удаляю 'red'
del colorsArr[1]          # удаляю 'black' (он после удаления red стал [1] элментом)
print (colorsArr)         # ['green', 'gray']
