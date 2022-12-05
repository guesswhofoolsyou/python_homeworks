# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

import random

def create_num ():
    num = random.randint(0, 10)
    return num

def create_list(num):
    array = []
    for i in range (0, num):
        array.append(round((random.random()*10),2))
    return array

def find_the_differense(array):
    max_el = max(array)
    print ('Максимальный элемент:',max_el)
    min_el = min(array)
    print ('Минимальный элемент:',min_el)
    dif = abs(round((max_el - int(max_el)) - (min_el - int(min_el)), 3))
    return dif

length = create_num()
print ('Длина списка равно:', length)
new_list = create_list(length)
print (new_list)
differ = find_the_differense(new_list)
print (differ)