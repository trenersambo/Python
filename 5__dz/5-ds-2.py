import random

play1 = input('Игрок №1, твоё имя: ')
play2 = input('Игрок №2, твоё имя: ')

# 1. ф-ция ЖЕРЕБЬЕВКИ (кто первым ходит)
def getLotRandom():


    lotRandom = random.randint(1, 2)  # Жребий: кто играет первый
    print(f'Рандомное число: {lotRandom}')

    if lotRandom == 1:
        print(f'Первый ходит {play1} (№ {lotRandom})')
        return (lotRandom)  # вернуть значение 1
    elif lotRandom == 2:
        print(f'Первый ходит {play2} (№ {lotRandom})')
        return (lotRandom) # вернуть значение 2




# 2. ф-ция ХОДОВ ИГРОКОВ (аргумент = lot):
def turn(lot): # 1 or 2

    candyTotal = 100  # (на старте) Кол-во конфет в игре
    candyLimit = 28     # лимит взятия конфет

    arrPlay1 = []
    arrPlay2 = []

    # игра до тех пор, пока КонфетыТотоал > 0
    while candyTotal >=0:

        # Для ИГРОКА № 1
        if lot == 1 :

            takeCandy = int(input(f'{play1} (игрок №1), сколько берешь (max=28): '))

            #print(candyTotal, takeCandy)

            while ( takeCandy > 28) or (candyTotal - takeCandy < 0):
                print(f'Кол-во конфет м.б. от 1 до 28, или конфет на остатке меньше чем берете')
                takeCandy = int(input('Взять (max=28): ') )

            # остается конфет после хода
            candyTotal = candyTotal - takeCandy

            print(f'Игрок №{lot} взял {takeCandy} шт. Конфет осталось: {candyTotal} \n')

            # Сколько конфет сейчас у Игрока № 1
            arrPlay1.append(takeCandy)

            #  смена хода--> на игрока № 2 (ч/з замену переменной lot)
            #  Но условие, если конфет остальось не НОЛЬ
            if candyTotal>0:
                lot = 2

            elif candyTotal==0:
                print(f'{play1} - игрок №{lot} победил')
                break






        # Для ИГРОКА № 2
        if lot == 2:

            takeCandy = int(input(f'{play2} (игрок №2) берёт (max=28): '))

            #print(candyTotal, takeCandy)

            while ( takeCandy > 28) or (candyTotal - takeCandy < 0):
                print(f'Кол-во конфет м.б. от 1 до 28, или конфет на остатке меньше чем берете')
                takeCandy = int(input('Взять (min = 1, max=28): ') )

            # остается конфет после хода
            candyTotal = candyTotal - takeCandy

            print(f'Игрок №{lot} взял {takeCandy} шт. Конфет осталось: {candyTotal} \n')

            # Сколько конфет сейчас у Игрока № 2
            arrPlay2.append(takeCandy)

            #  смена хода--> на игрока № 2 (ч/з замену переменной lot)
            #  Но условие, если конфет остальось не НОЛЬ
            if candyTotal > 0:
                lot = 1

            elif candyTotal == 0:
                print(f'{play2} - игрок №{lot} победил')
                break














# =============================================
# раздел вызова функций

# 1. вызов ф-ции ЖЕРЕБЬЕВКИ (кто первым ходит)
lot = getLotRandom()

# 2. вызов ф-ции ХОДОВ ИГРОКОВ (аргумент = №, имяИгрока), lot =1 или =2:
turn( int(lot) )

