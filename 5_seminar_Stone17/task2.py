# в файле  n натур. чисел через пробел записаны
# не хватает одного числа

#  1 2 3 4 5 ... 7 8 9

# Порчиать файл и  вывести в консоль (6)

with open(r'text.txt', 'r') as data:
    text = data.read().split()
print(text)

text = list(map(int,text))
print(text)

for i in range(1,len(text)):
    print(f'{i}-е число: {text[i]}')
    print(f' : {text[i]-1} = {text[i-1]}')
    if text[i]-1 != text[i-1]:

        print(f'Искомое число: {text[i]-1}' )