# Есть список случайных чисел в промежутке от 1 до 200, количеством 200. 
# Создайте список кортежей, первый элемент которого - индекс элемента, а второй - сам элемент, при условии, что они не совпадают.

import random

def add_list():
    user_list = []
    while True:
        try:
            num = int(input('Введите кол-во элементов списка: '))
        except ValueError:
                print('Это не число. Давай по новой.')
        else:
            break
    for i in range (0, num):
        user_list.append(random.randrange(1,200))
    return user_list

def listing(user_list):
    result_list = []
    result_num = []
    for i in range (0, len(user_list)):
        if i != user_list[i]:
            result_list.append(user_list[i])
            result_num.append(i+1)
    zip_tuple = list(zip(result_num, result_list))
    return zip_tuple

user_list = add_list()
print (user_list)
print (listing(user_list))