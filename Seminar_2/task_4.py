# По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого.
# При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, остальные получили по две монеты.
# Далее человек, на котором остановился счет, отдает все свои монеты следующему по счету человеку, а сам выбывает из круга.
# Процесс продолжается с места остановки аналогичным образом до последнего человека в круге. Составьте алгоритм, который проводит эту игру.
# Если хотите делать паузы, то импортируйте библиотеку time и используйте оттуда функцию sleep.
# Определите номер этого человека и количество монет, которые оказались у него в конце игры.

# пока не вышло, но её победю))

import random

def players_coins(num):
    array = []
    for i in range (0, num-1):
        array.append(0)
    return array

def who_s_lost (array, amount):
    num = random.randrange(1, 10)
    print ("Счет заканчивается на:",num)
    while num > amount:
        num = num - amount
    while amount != 1:
        for i in range (0, amount-1):
            if i < num:
                array[i] +=1
            elif i > num:
                array[i] +=2
            else:
                array.remove(i)
        amount -=1
        print(i)
    print (array)

amount_of_players = int(input("Введите кол-во участников:\n"))
player = players_coins(amount_of_players)
who_s_lost(player, amount_of_players)