#  ========  задача №2   (из он-лайн задачников по Python) ==========

# состоит ли число из одинаковых цифр


# ========= Решение № 1 (easy) =============================

num = input()
size = len(num)
flag = False

for i in range(size):
    if num[i] == num[size - 1] or num[i] == num[i + 1]:
        flag = True
    else:
        flag = False
        break

print('YES' if flag else 'NO')



# ========= Решение № 2 (enumerate) =============================

def sameDigits(numArr):

   # print(numArr)

   for i, el in enumerate(numArr):

       if el !=numArr[len(numArr)-1]:
           print('NO')
           break
   else:
       print('YES')


numArr = list(map(int, input()) ) # преобразование на лету в массив
sameDigits(numArr)