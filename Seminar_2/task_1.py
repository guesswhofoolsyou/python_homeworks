# Exercise #2.1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

import random


def sum_of_digits(num):
    result = 0
    array_num = str(num)
    for i in range(len(array_num)):
        if array_num[i] != ",":
            result += int(array_num[i])
        else:
            continue
    print('Сумма цифр в числе',num,':\n',result)


num=input('Введите число:\n')
sum_of_digits(num)


