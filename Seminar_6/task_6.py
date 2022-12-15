# Из списка выше оставьте только те пары, где сумма кортежа кратна 5

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
    zip_list = list(zip(result_num, result_list))
    return zip_list

def cut_the_list(zip_list):
    result_index_list = []
    result_digits_list = []
    index_list, digit_list = zip(*zip_list)
    for i in range(0, len(index_list)):
        sum1 = 0
        sum2 = 0
        temp = index_list[i]
        tmp = digit_list[i]
        while (tmp != 0):
            sum1 += tmp % 10
            tmp = tmp // 10
        if index_list[i] > 9:
                while (temp != 0):
                    sum2 += temp % 10
                    temp = temp // 10
        else:
            sum2 += index_list[i]
        if (sum1 + sum2) % 5 == 0:
            result_index_list.append(index_list[i])
            result_digits_list.append(digit_list[i])
    zip_zip_list = list(zip(result_index_list, result_digits_list))
    return zip_zip_list


user_list = add_list()
print (user_list)
zip_list = listing(user_list)
print (zip_list)
print (cut_the_list(zip_list))