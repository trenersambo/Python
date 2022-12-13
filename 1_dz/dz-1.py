dayWeek = ['Понед','Вторн' ,'Среда' ,'Четверг' ,'Пят-ца' ,'Субб' ,'Вскр-е']

day = int(input('введи день недели (от 1 до 7): '))
# print(f'введен день недели: {day}')
# print(type(day))

# idx = dayWeek.index(day)
# print(type(idx))

while day<=0 or day>=8:
    print('Написано же, введи число от 1 до 7')
    day = int(input('введи день недели (от 1 до 7): '))


for d in dayWeek:
     # print (f'Индекс в Списке: {dayWeek.index(d)}, День недели: {d} ')
     # print(type(dayWeek.index(d) ) )
     if (day - 1) == int(dayWeek.index(d)):
         print(f'Выбрал: {d}')

if (day - 1) == 5 or (day - 1) == 6:
    print('И это - выходной день!')


