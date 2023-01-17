# Делители-1
# На вход программе подается два натуральных числа a и b  (a<b ).
# Напишите программу, которая находит натуральное число
# из отрезка [a,b] с максимальной суммой делителей.
#
# На вход программе подаются два числа, каждое на отдельной строке.
#
# Программа должна вывести два числа на одной строке, разделенных пробелом:
#  число с максимальной суммой делителей и сумму его делителей.
#
# Если таких чисел несколько, то выведите наибольшее из них.


#  ================  Решение № 1 (обычное)  ===============================

def maxDivder(numArr):
   a,b = numArr            # a=10 b=20

   count = 0       # счётчик
   maxSumm = 0     # макс. сумма
   accumArr = [0, 0]   # итоговый массив

   for i in range(a, b+1):

       for j in range(1, b+1):

           if (i % j == 0):
               print(f'для {i} делитель {j}')

               count +=1
               maxSumm +=j

       print(f'Для {i} count={count}, макс.сумм={maxSumm}')


       if (count >= accumArr[0]) or (maxSumm >= accumArr[1]):
           accumArr[0] = i
           accumArr[1] = maxSumm


       # обнулить: count,  maxsumm (чтоб с нуля считать другое число)
       count = 0
       maxSumm = 0



       print('')

   #print(accumArr)
   print(f'{accumArr[0]} {accumArr[1]}')

numArr = [int(input()) for i in range(2)]
maxDivder(numArr)



#  ================  Решение № 2  (sorted)  ===============================

def summ(a):
	return sum([i for i in range(1, a + 1) if a % i == 0])

a, b = int(input()),  int(input())
numbers = sorted([ i for i in range(a, b + 1)], reverse = True)

sum_del = [summ(i) for i in numbers]
max_index = sum_del.index(max(sum_del))

print(numbers[max_index], sum_del[max_index])


#  ================  Решение № 3  (array / list)  ===============================

z=[]
x=[]
a=[]
for i in range(int(input()), int(input())+1):
    for _ in range(1, i+1):
        if i%_==0:
            z.append(_)
    x.append(sum(z))
    z=[]
    a.append(i)
if x.count(max(x))==1:
    print(a[x.index(max(x))], max(x))
else:
    x=x[::-1]
    a=a[::-1]
    print(a[x.index(max(x))], max(x))

