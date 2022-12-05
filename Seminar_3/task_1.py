# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def create_num ():
    num = random.randint(0, 10)
    return num

def create_list(num):
    array = []
    for i in range (0, num-1):
        array.append(random.randrange(0, 10))
    return array

def sum_of_a_list (array):
    summ = 0
    for i in range (0, len(array)):
        if i % 2 == 1 :
            summ += array[i]
    return summ

length = create_num()
print ('Длина списка равно:', length)
new_list = create_list(length)
print (new_list)
summ = sum_of_a_list(new_list)
print ('Сумма нечетных элементов:', summ)