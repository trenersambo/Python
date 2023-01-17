# Ваша задача — создать функцию, которая выполняет четыре основные математические операции.
#
# Функция должна принимать три аргумента - операция(строка/символ), значение1(число), значение2(число).
# Функция должна возвращать числовой результат после применения выбранной операции.
#
# Примеры(Оператор, значение1, значение2) --> вывод
# ('+', 4, 7) --> 11
# ('-', 15, 18) --> -3
# ('*', 5, 5) --> 25
# ('/', 49, 7) --> 7


# def basic_op(numAndSym):
#     a,b,s = numAndSym
#     a = str(a)
#     b = int(b)
#     s = int(s)
#
    # if a == '+':
    #     return s + b
    # if a == '-':
    #     return b - s
    # if a == '*':
    #     return s * b
    # if a == '/':
    #     return b / s
#
# numAndSym = [input() for i in range(3)]
# basic_op(numAndSym)


def basic_op(operator, value1, value2):
    #your code here
    #print(operator, value1, value2)

    if operator == '+':
        return value1 + value2
    if operator == '-':
        return value1 - value2
    if operator == '*':
        return value1 * value2
    if operator == '/':
        return value1 / value2

# !!!! в Code Wars не надо вводить вводимые данные и вызывать ф-цию !!!
# operator = input()
# value1 = int(input())
# value2 = int(input())
#
# basic_op(operator, value1, value2)




# варианты решений 1 :

def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))

# варианты решений 2 :

def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))

# варианты решений 3 :

def basic_op(operator, value1, value2):
    return eval(f'{value1}{operator}{value2}')

# варианты решений 4 :

def basic_op(operator, value1, value2):
    ops = {'+': lambda a, b: a + b,
           '-': lambda a, b: a - b,
           '*': lambda a, b: a * b,
           '/': lambda a, b: a / b}
    return ops[operator](value1, value2)

# варианты решений 5 :

def basic_op(operator, value1, value2):
    return {
    "+": value1 + value2,
    "-": value1 - value2,
    "*": value1 * value2,
    "/": value1 / value2,
    }[operator]

# варианты решений 6 :

basic_op = lambda o,a,b: eval(str(a)+o+str(b))

