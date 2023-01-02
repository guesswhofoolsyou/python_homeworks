from typing import Union
import checks
import const
import logic
import logger

# Вывод меню в терминал

def print_menu() -> str:
    data = list(enumerate(const.MENU))
    print('Выберите пункт меню:')
    for i, value in data:
        print(f'{i}. {value}')
    choice = checks.int_num('', -1, data[-1][0])
    return data[choice][1]

# Выбор типа вводных чисел

def choose_value() -> str:
    data = list(enumerate(const.VALUE))
    print('Выберите тип чисел:')
    for i, value in data:
        print(f'{i}. {value}')
    choice = checks.int_num('', -1, len(const.VALUE))
    return data[choice][1]

# Ввод аргументов в терминале

def input_arguements(type : str) -> Union[float, complex]:
    if type == const.VALUE[0]:
        return checks.float_num('Введите вещественное число:\n')
    elif type == const.VALUE[1]:
        return checks.complex_num()

# Выбор операции

def operation():
    data = list(enumerate(const.OPERATION))
    print('Введите операцию из перечисленных ниже:')
    for i, value in data:
        print(f'{i}. {value}')
    try:
        oper = input()
        if oper not in ['+', '-', '*', '/']:
            print('Введите операцию: ')
        return oper
    except:
        print('Вы ввели неверную операцию! Попробуйте снова.')

# Вычисление

def oper_result(x, y, operation_value):
    if operation_value == const.OPERATION[0]:
        result = logic.sum(x, y)
    elif operation_value == const.OPERATION[1]:
        result = logic.sub(x, y)
    elif operation_value == const.OPERATION[2]:
        result = logic.mltpl(x, y)
    elif operation_value == const.OPERATION[3]:
        result = logic.div(x, y)
    logger.write_in_log(f'{x}\{operation_value}\{y}\{result}\n')
    print (f'{x}{const.OPERATION[operation_value]}{y}={result}')
    return result