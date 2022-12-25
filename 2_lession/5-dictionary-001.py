# 5. Словари

dictionary = {}      # создать пустой словарь

dictionary = \
    {                # / делает перенос строки
        'up': '↑',   # ключ: "значение"
        'left': '←', # ключ: "значение"
        'down': '↓', # ключ: "значение"
        'right': '→' # ключ: "значение"
    }
print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left'])  # ←
# типы ключей могут отличаться

dic = {}

dic = \
    {
        'one': 'SAMBO',
        'two': 'BJJ',
        'three': 'judo'
    }

# просмотр ключей
for k in dic.keys():
    print(k )   #one two three

# просмотр значений ключей (вариант 1)
for p in dic.values():
    print(p)    #SAMBO BJJ judo

# просмотр значений ключей (вариант 2)
for v in dic:
    print(dic[v])    #SAMBO BJJ judo