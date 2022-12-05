# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

import random

def create_num():
    num = random.randint(2, 10)
    return num

def convert_num(first_num):
    if first_num == 0:
        return result_list
    result_list.append(first_num % 2)
    convert_num(first_num // 2)


unbinary_num = create_num()
print('Десятичное число:',unbinary_num)
result_list = []
convert_num(unbinary_num)
print (result_list)
result_list.reverse()
result_num = ''.join(str(n) for n in result_list)
print ('Двоичное число:',result_num)