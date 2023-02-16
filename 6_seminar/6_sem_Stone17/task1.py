# вывод только уникальных чисел из списка
import random
lst = [random.randint(0,10) for _ in range(15)]
print(lst ) #[4, 3, 4, 4, 9, 6, 0, 8, 0, 0, 5, 6, 0, 0, 6]


for i in range(len(lst)):


    count = 0

    for j in range(len(lst)):

        if lst[i]==lst[j] and i != j:
            print(f'{lst[i]}=={lst[j]} and  {i} != {j}')
            count +=1

    if count <1:
        print(f'{lst[i]}, счётчик: {count} ' )