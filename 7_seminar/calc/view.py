import logger

def ViewData(data):
    logger.Log('controller.ClickButtom_v2', 'view.ViewData', data)
    logger.Log('view.ViewData', 'controller.ClickButtom_v2', data)
    print(f'= {data}')


def GetUserValue_v1():
    user_input = float(input('Enter value: '))
    logger.Log('controller.ClickButtom_v2', 'view.GetUserValue_v1', 'null')
    logger.Log('view.GetUserValue_v1', 'controller.ClickButtom_v2', user_input)
    return user_input


def GetUserFunction():
    user_input = input('Enter function ("+", "-", "*", "/", "C"): ')
    logger.Log('controller.ClickButtom_v2', 'view.GetUserFunction', 'null')
    logger.Log('view.GetUserFunction', 'controller.ClickButtom_v2', user_input.upper())
    return user_input

