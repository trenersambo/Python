# 4 Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой четверти (x и y).

# В 1: (x >0 и y>0 ): +∞ до +∞;
# В 2: (x < 0, y > 0): -∞ до +∞
# в 3: (x < 0, y < 0): -∞ до -∞
# в 4: (x > 0, y < 0): +∞ до -∞

# ============ РЕШЕНИЕ ==============

 
def dekart_plane(num):
    print(f'указан {num}-й номер четверти' )
    
    for el in diapazon:
      if(num-1)==int(diapazon.index(el)):
        print(f'Возможный диапазон: {el}')


num = int(input("Укажи четверть Декартовой системы координат (от 1 до 4): "))

if  num<=0 or num>=5:
  print('Надо ввести: от 1 до 4')
  #stop # не срабатывает

diapazon = [
'(0 до +∞, 0 до +∞)',
'(0 до -∞, 0 до +∞)',
'(0 до -∞, 0 до -∞)',
'(0 до +∞, 0 до -∞)'
]

dekart_plane(num)