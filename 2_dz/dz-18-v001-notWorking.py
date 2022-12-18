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
    for i in array:
        idxRndm = random.randint(minEl, maxEl)  # создание рандомного индекса
        #print(idxRndm, end=' | ')  # рандомн.знач. индексов от 0 до 7

        #print(i, array[i-1])    # 1,1   2,2 ...  7,7    8,8

        tmp = i     # сохр.текущее значение во временн.переменную
        print(f'TMP: {tmp} => индекс для {array[i-1]}: { array.index(i) }')

        print(f'Рандом. индекс {idxRndm}: значение массива { array[idxRndm] }')

        print(f'i ДО замены = {i} ')
        i = array[idxRndm]
        print(f'i ПОСЛЕ замены = {i} \n')

        #print(array.index(idxRndm))

        # array.index(i) = tmp

        print(array)







shuffleArr([1,2,3,4,5,6,7,8])