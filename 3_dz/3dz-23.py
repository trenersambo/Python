# print('дмашнее задание №2 к семинару 3')

#1. вызов ф-ции
def my_list(arr):
    print(arr) # --> [2, 3, 4, 5, 6]
    print(f'Длинна массива len = { len(arr) } ')
    print(f'Последний индекс массива: {len(arr)-1} ')
    print(f'Последнее число массива: {arr[len(arr)-1]}' )
    print(f'Первое число массива: {arr[0]} , {type(arr[0])} \n')

    # Для поиска границы отсечения
    # если массив % 2 > 0 , то просто (len(arr) / 2)
    # если массив % 2 == 0 , просто (len(arr) / 2)-1
    # print ( int(len(arr) / 2) )

    # переменные (старт.данные), которые буду увеличивать вправо / уменьш влево
    leftIdx = 0
    rightIdx = (len(arr)-1)

    # До тех пор, пока ЛевИндекс не сравняется с ПравИндексом
    while(leftIdx <= rightIdx):

        print(f'ЛевИндекс:{leftIdx} , ПравИндекс:{rightIdx}')

        # выполнение условия задачи
        multi = (arr[leftIdx])*(arr[rightIdx])
        print(f'ЧислоЛевое: {arr[leftIdx]}, ЧислоПравое: {arr[rightIdx]}')

        print(f'Итог умножения: {multi} \n')

        # сближение индексов в каждом круге
        leftIdx +=1
        rightIdx -=1


# задан Список (массив ) my_list
my_list([2,3,5,6])
my_list([2,3,4,5,6])