import view
import operation_logic
import logger


a = 0
func = ''
b = 0


def ClickButtom_v1(): # одно вычисление -> число, операция, число
    logger.Log('main', 'controller.ClickButtom_v1', '__Start__')
    global a
    global func
    global b
    a = view.GetUserValue_v1()
    func = view.GetUserFunction()
    b = view.GetUserValue_v1()
    result = operation_logic.FunctionLogic(func, a, b)
    view.ViewData(result)
    logger.Log('controller.ClickButtom_v1', 'main', '__End__')


def ClickButtom_v2(): # повторяющиеся одинарные вычисления -> результат, операция, число
    logger.Log('main', 'controller.ClickButtom_v2', '__Start__')
    global a
    global func
    global b
    a = view.GetUserValue_v1()
    func = view.GetUserFunction()

    while func.lower() != 'c':
        b = view.GetUserValue_v1()
        result = operation_logic.FunctionLogic(a, func, b)
        view.ViewData(result)
        a = result
        func = view.GetUserFunction()
    logger.Log('controller.ClickButtom_v2', 'main', '__End__')

