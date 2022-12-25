# === Пример 6.2. базовый API работы с set ===

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

c = a.copy()  # КОПИЯ
print(c)      #  c = {1, 2, 3, 4, 5}

u = a.union(b) # ОБЪЕДИНЕНИЕ
print(u)       # u = {1, 2, 3, 4, 5, 6, 7, 8}

i = a.intersection(b) #  ТОЛЬКО СОВПАДЕНИЯ
print(i)              # i = {4, 5}

dl = a.difference(b)  #  ЕСТЬ ТОЛЬКО В МНОЖЕСТВЕ a
print(dl)             # dl = {1, 2, 3}

dr = b.difference(a)  #  ЕСТЬ ТОЛЬКО В МНОЖЕСТВЕ b
print(dr)             # dr = {8, 6, 7}

q = a \
    .union(b) \
    .difference(a.intersection(b))
# {1, 21, 3, 13}

s = frozenset(a) # заморозка

