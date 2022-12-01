# Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.
# Пример:
# # - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

from random import randint

def fill_random_array(num):
    result_array = [randint(-10,11) for x in range(num)]
    return result_array

def fill_zero (array, num):
    result_array = []
    array_length = num
    counter = 0
    for i in range (0, array_length):
        if array[counter] < 0:
            result_array[i] = array[counter]
            result_array[i+1] = 0
            array_length += 1
            counter += 1
            i += 1
        elif array[counter] >= 0:
            result_array[i] = array[counter]
    print (result_array)


num = int(input("Введите длину массива:\n"))
array = fill_random_array(num)
print(array)
result_array = fill_zero(array, num)