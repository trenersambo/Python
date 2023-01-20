import logger


def PlusFunction(x, y):
    logger.Log('operation_logic.FunctionLogic', 'functions.PlusFunction', (x, y))
    logger.Log('functions.PlusFunction', 'operation_logic.FunctionLogic', x + y)
    return x + y


def MinusFunction(x, y):
    logger.Log('operation_logic.FunctionLogic', 'functions.MinusFunction', (x, y))
    logger.Log('functions.MinusFunction', 'operation_logic.FunctionLogic', x - y)
    return x - y


def MultiplicationFunction(x, y):
    logger.Log('operation_logic.FunctionLogic', 'functions.MultiplicationFunction', (x, y))
    logger.Log('functions.MultiplicationFunction', 'operation_logic.FunctionLogic', x * y)
    return x * y


def DivisionFunction(x, y):
    logger.Log('operation_logic.FunctionLogic', 'functions.DivisionFunction', (x, y))
    logger.Log('functions.DivisionFunction', 'operation_logic.FunctionLogic', x / y)
    return x / y

