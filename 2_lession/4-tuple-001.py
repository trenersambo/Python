t = ()
print(type(t))      # tuple

t = (1,)
print(type(t) , t)  # tuple (1,)

t = (1)
print(type(t), t )  # int 1

t = (18, 11, 1937)
print(type(t))      # tuple

colors = ['Самбо', 'рулит', '4ever']
print(colors)       # ['Самбо', 'рулит', '4ever']

t = tuple(colors)
print(t)            # ('Самбо', 'рулит', '4ever')
print(t[0], t[-3])  # Самбо  Самбо




# ===== Перебор через for ======

t = tuple(['red', 'green', 'blue'])

for e in t:
    print(e)     # red green blue

#t[0] = 'black'   # TypeError: 'tuple' object does not support item assignment

print(t[0])      # red
print(t[2])      # blue
# print(t[10])   # IndexError: tuple index out of range
print(t[-2])     # green
# print(t[-200]) # IndexError: tuple index out of range