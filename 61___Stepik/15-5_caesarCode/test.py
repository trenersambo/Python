import re
t = 'Day, mice. "Year" is a mistake!'

arr = t.split(' ')
print(arr)
#
# arj = ' '.join(arr)
# print(list(arj))


arrLen = []
for i in range(len(arr)):
    arr[i] = re.sub(r'[,."!]', "" , arr[i])
    arrLen.append(len(arr[i]))

print(arrLen)