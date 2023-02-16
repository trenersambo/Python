# #  распарсить и выполнить матем. действие:
#
# 2 + 2 = > 7
# 1 + 2 * 3 -> 7
# 1 - 2 * 3 -> -5

st = '1 + 2 * 3'
newSt = st.split(' ')
print(newSt)           # ==> ['1', '+', '2', '*', '3']

arr = []


for i in range(len(newSt)):
    if newSt[i].isdigit():
        arr.append(int(newSt[i]))
    else:
        arr.append(newSt[i])

print(arr)












