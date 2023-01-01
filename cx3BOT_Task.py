# =================================
# Задача
# сформировать строку из 10 символов
# на четных позициях д.б. четные цифры
# на нечтеных - буквы

# string = 'abcdefghjk'
# arr = list(string)
# print(arr)               # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k']
#
# for idx in range(len(arr)):
#
#     print(idx, arr[idx]) # индекс / значение (до замены)
#
#     if idx % 2 == 0:
#         arr[idx] = idx   # замена на четную цифру (на свой четный индекс)
#
# print(arr)



# ================================

# Задача

# Дана строка
# Покажи номера символов, совпадающих с последним символом строки

string = 'aFRfrTfFsf'
string = string.upper() # aFRfrTfFsf --> AFRFRTFFSF

arrStr = list(string)  # ['A', 'F', 'R', 'F', 'R', 'T', 'F', 'F', 'S', 'F']
print(arrStr)

lastEl = arrStr[len(arrStr)-1] # F

accEl = []

for i in range( len(arrStr) ):
    print(i, arrStr[i]) # индекс / значение

    if arrStr[i] == lastEl:
        accEl.append(i) # все совпадение скинул в массив

print(f' Массив совпавших символов: {accEl}') # [1, 3, 6, 7, 9]

s = ' '.join(map(str, accEl))
print(f' Номера совпавших символов: {s}') # 1 3 6 7 9





