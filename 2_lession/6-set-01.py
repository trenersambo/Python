# === Пример 6.1. базовый API работы с set ===

colors = {'red', 'green', 'blue'}
print(colors)       # {'red', 'green', 'blue'}

colors.add('red')   # попытка создать ДУБЛЬ 'red'
print(colors)       # {'red', 'green', 'blue'}

colors.add('gray')  # ДОБАВИТЬ 'gray'
print(colors)       # {'red', 'green', 'blue','gray'}

colors.remove('red')  # УДАЛИТЬ 'red'
print(colors)         # {'green', 'blue','gray'}

# colors.remove('red') # KeyError: 'red' (нечего удалять)

colors.discard('red')  # ok
print(colors)          # {'green', 'blue','gray'}

colors.clear()   # { } ОЧИСТКА множества
print(colors)    # set()

