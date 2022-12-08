# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

import random
import math

def create_num():
    num = random.randint(1, 100)
    return num


# функция создает набор простых чисел в диапозоне от 0 до num
def setting_digits(num):
    set_of_simple_nums = []
    for i in range(num + 1):
        set_of_simple_nums.append(i)
    i = 2
    while i <= num:
        if set_of_simple_nums[i] != 0:
            j = i + i
            while j <= num:
                set_of_simple_nums[j] = 0
                j = j + i
        i += 1
    set_of_simple_nums = set(set_of_simple_nums)
    set_of_simple_nums.remove(0)
    set_of_simple_nums = list(set_of_simple_nums)
    return set_of_simple_nums


# проверяем на какой элемент из списка число делится нацело
def check_simple_nums(num, some_list):
    result_list = []
    for i in range (0, len(some_list)):
        if num % some_list[i] == 0:
            result_list.append(some_list[i])
    return result_list


num = create_num()
print ('Вводимое число:', num)
array_of_nums = setting_digits(num)
print (array_of_nums)
result_array = check_simple_nums(num, array_of_nums)
print (result_array)
