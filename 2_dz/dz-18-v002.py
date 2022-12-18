# Задача № 5.

#Перемешать  массив

def shuffleArr(array):
    #print(array, array[0])      #[1, 2, 3, 4, 5, 6, 7, 8]     1

    print(f'Массив для перемешивания: {array}')

    # Подготовка к работе рандомайзера
    minEl = 0                # миним. индексМассива = 0
    maxEl = len(array)-1     # макс. индексМассива

    print(f'Мин.индекс: {minEl} , макс. индекс: {maxEl}')    # стартМассива: 1 конецМассива:8

    import random   # Импорт модуля для рандомайзера
    for i in range(maxEl):
        idxRndm = random.randint(minEl, maxEl)  # создание рандомного индекса
        print(f'Рандомный индекс: {idxRndm} ')  # рандомн.знач. индексов от 0 до 7


        val1 = array[idxRndm]
        vav2 = array[idxRndm - 1]
        # print(f'Значения : array[idxRndm]={array[idxRndm]}')
        # print(f'Значения : array[idxRndm-1]={array[idxRndm-1]}')

        array[idxRndm - 1] = val1
        array[idxRndm] = vav2

    print(f'Массив после перемешивания: {array}')



shuffleArr([1,2,3,4,5,6,7,8])