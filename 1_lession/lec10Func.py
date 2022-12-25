#=============
#=============Пример 10. Функции
 

def foo(x):
    return x**5

arg = 3
print(foo(arg)) # 3**5 = 243



#Задача 10.2. Применить / поиграться с функцией..

def fo(x,y):
    if x == y:
        return "Равны"
    elif x+5 < y:
        return f'{x} < {y}'
    else:
        return y

arg1 = 2
arg2 = 20

print(fo(arg1,arg2))  # 2 < 20
