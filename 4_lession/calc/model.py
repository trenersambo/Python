
# суммируем  числа (умнож, делен,...)
# логика

x = 0
y = 0

# инициализация и глобализация переменных
def init(a,b):
    global x
    global y

    x = a
    y = b

def mathem():
    return x + y
