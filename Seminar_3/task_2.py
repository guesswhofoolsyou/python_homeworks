# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

def create_num ():
    num = random.randint(0, 10)
    return num

def create_list(num):
    array = []
    for i in range (0, num):
        array.append(random.randrange(0, 10))
    return array

def multiply_of_pairs(array):
    multiply = []
    el = len(array)
    if el % 2 == 1:
        pairs = el // 2 + 1
    else:
        pairs = el // 2
    for i in range (0, (pairs)):
        multiply.append(array[i]*(array[el-1-i]))
    return multiply

length = create_num()
print ('Длина списка равно:', length)
new_list = create_list(length)
print (new_list)
mult = multiply_of_pairs(new_list)
print (mult)
