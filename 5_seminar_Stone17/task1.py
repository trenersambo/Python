# Удалить слова где есть буквы "абв"

strg = 'Питон  пожалуабвй лучший из абвхудших языков в мире'

strg = strg.split()

newList = []

for w in strg:
    if not 'абв'in w:
        newList.append(w)

print(' '.join(newList))

# # вариант №2 (не сработал)
#
# st = 'Питон  пожалуабвй лучший из абвхудших языков в мире'
#
# arr = list(filter(lambda w: not 'aбв' in w , st))
#
#
# print(''.join(arr))



# вариант №3
s  = 'Питон  пожалуабвй лучший из абвхудших языков в мире. набве все будет ок'

nl = [x for x in s.split() if not 'абв' in x]
print(' '.join(nl))