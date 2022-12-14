 # Задача №5
 #
 # Напишите программу,
 # которая принимает на вход координаты двух точек и
 # находит расстояние между ними в 2D пространстве

 #  Формула для решения: AB = √(xb - xa)^2 + (yb - ya)^2

 # ========= Решение: ===================
def result(xa, xb, ya, yb):
    import math
    distance = math.sqrt( ( (xb - xa) **2 ) + ( (yb-ya)**2 )  )
    print(f'Расстояние между {xa, ya} и {xb, yb}: {round(distance, 3) }' )

xa = float(input('Введи координату x для точки А: '))
xb = float(input('Введи координату x для точки B: '))

ya = float( input('Введи координату y для точки А: '))
yb = float( input('Введи координату y для точки B: '))

result(xa, xb, ya, yb)
