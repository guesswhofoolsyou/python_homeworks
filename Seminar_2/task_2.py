# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def multiply_of_sequence(num):
    result = []
    mult = 14 
    for i in range(1, num+1):
        if i==1:
            result.append(1)
        else:
            mult=mult*i
            result.append(mult)
    print(result)

num = int(input("Введите число:\n"))
multiply_of_sequence(num)