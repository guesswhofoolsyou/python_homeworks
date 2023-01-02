from typing import Optional


# функция возвращает целое число
# input_num: ввод числа с клавиатуры
# min_num: минимальное значение
# max_num: максимально значение
# return: возвращает целое число в промежутке от min_num до max_num

def int_num(input_num: str,
            min_num: Optional[int] = None,
            max_num: Optional[int] = None, ) -> int:

    # Проверка на дурака

    while True:
        try:
            num = int(input(input_num))
            if num not in range(min_num, max_num + 1):
                print(f'Введите число от {min_num} до {max_num}')
                continue
            return num
        except ValueError:
            print('Вы ввели неверное значение! Попробуйте снова.')

# функция возвращает вещественное число
# input_num: ввод числа с клавиатуры
# min_num: минимальное значение
# max_num: максимально значение
# return: возвращает вещественное число в промежутке от min_num до max_num


def float_num(input_num: str,
              min_num: Optional[int] = None,
              max_num: Optional[int] = None, ) -> float:

    # Проверка на дурака

    while True:
        try:
            num = float(input(input_num))
            if (min_num and max_num) and num not in range(min_num, max_num + 1):
                print(f'Введите число от {min_num} до {max_num}')
                continue
            return num
        except ValueError:
            print('Вы ввели неверное значение! Попробуйте снова.')

# функция возвращает комплексное число


def complex_num(min_num: Optional[int] = None,
                max_num: Optional[int] = None, ) -> complex:

    # Проверка на дурака

    while True:
        try:
            num = complex(real=float_num('Введите вещественную часть числа:\n'),
                          im=float_num('Введите мнимую часть числа:\n'))
            if num not in range(min_num, max_num + 1):
                print(f'Введите число от {min_num} до {max_num}')
                continue
            return num
        except ValueError:
            print('Вы ввели неверное значение! Попробуйте снова.')
