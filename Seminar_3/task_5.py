# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

import random

def create_num():
    num = random.randint(2, 10)
    return num


def fib(length):
    first_num = 0
    second_num = 1
    fib_list = []
    fib_list2 = []
    for i in range(length):
        first_num, second_num = second_num, first_num + second_num
        fib_list.append(first_num)
    for i in range (length):
        if i % 2 == 0:
            fib_list2.append(-fib_list[i])
        else:
            fib_list2.append(fib_list[i])
    fib_list2.reverse()
    fib_list2.append(0)
    result_fib = fib_list2 + fib_list
    return result_fib

length = create_num()
print ('Длина списка равно:', length)
fib_list = fib(length)
print (fib_list)