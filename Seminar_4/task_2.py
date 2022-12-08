# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

import random

def create_num():
    num = random.randint(10, 20)
    return num

def create_list(num):
    new_list = []
    for i in range (0, num):
        new_list.append(random.randint(1,5))
    new_list.sort()
    return new_list

num = create_num()
print ('Длина последовательности:',num)
sequence = create_list(num)
print (sequence)
short_sequence = list(set(sequence))
print(short_sequence)


