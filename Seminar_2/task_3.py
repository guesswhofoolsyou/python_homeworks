# Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.
# Пример:
# # - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

from random import randint

def fill_random_array(num):
    result_array = [randint(-10,10) for x in range(num)]
    return result_array


def fill_zero (array, num):
    result_array = []
    array_length = num
    for i in range (0, array_length+1):
        if array[i] < 0:
            if i == len(array):
                array.append(0)
            else:
                array.insert(i+1, 0)    
        else:
            continue
    print (array)

num = int(input("Введите длину массива:\n"))
array = fill_random_array(num)
print(array)
fill_zero(array, num)