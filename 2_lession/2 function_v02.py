#  ==== Значения аргументов ф-ции по умолчанию ===

# def sport( name, count = 3):
#     return name * count
#
# print( sport('bjj' ))     #3 раза по умолчанию: bjj bjj bjj
# print( sport('sambo ', 5)) #5 раз: sambo sambo sambo sambo sambo
# print( sport(400))         # выведет цифру: 400 * 3 = 1200



#  ====  Передача не ограниченного кол-ва аргументов в функицю ===

def unlim_Args(*params):

    res: str = '' # (не обязательно) явное сообщение типа

    for i in params:
        res += i
    print(res)     # sambo best sport

# вызов ф-ции:
unlim_Args('sam', 'bo',' ', 'best ','sport')


