# Дан список случайных чисел. Оставьте только те, сумма цифр которых четна

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
        user_list.append(random.randrange(10,100))
    return user_list

def check_list(user_list):
    result_list = []
    for i in range (0, len(user_list)):
        sum = 0
        temp = user_list[i]
        while (temp != 0):
            sum += temp % 10
            temp = temp // 10
        if sum % 2 == 0:
            result_list.append(user_list[i])
    return result_list

user_list = add_list()
print (user_list)
print (check_list(user_list))