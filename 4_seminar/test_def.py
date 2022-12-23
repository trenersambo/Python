# =========== 1 вариант подключения=========

import sem41

list_num = input('Введите числа через пробел ->').split()

print(*sem41.find_min_max(list_num))

# =========== 2 вариант подключения=========

from  sem41 import find_min_max

list_num = input('Введите числа через пробел ->').split()

print(*find_min_max(list_num))
