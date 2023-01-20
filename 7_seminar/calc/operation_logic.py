import functions
import logger


def FunctionLogic(x, operation, y):
    logger.Log('controller.ClickButtom_v2', 'operation_logic.FunctionLogic', [x, operation, y])
    if operation == '+':
        result = functions.PlusFunction(x, y)
        logger.Log('operation_logic.FunctionLogic', 'controller.ClickButtom_v2', result)
        return result
    elif operation == '-':
        result = functions.MinusFunction(x, y)
        logger.Log('operation_logic.FunctionLogic', 'controller.ClickButtom_v2', result)
        return result
    elif operation == '*':
        result = functions.MultiplicationFunction(x, y)
        logger.Log('operation_logic.FunctionLogic', 'controller.ClickButtom_v2', result)
        return result
    elif operation == '/':
        result = functions.DivisionFunction(x, y)
        logger.Log('operation_logic.FunctionLogic', 'controller.ClickButtom_v2', result)
        return result

