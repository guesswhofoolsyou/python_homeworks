# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]


def get_sequence(n):
    result_array = []
    sum = 0
    for i in range(0, n):
        result_array.append((1+1/(i+1))**(i+1))
        sum += result_array[i-1]
    print(result_array)
    print(f"Сумма последовательности равна: {sum}")


length = int(input("Введите кол-во символов последовательности:\n"))
get_sequence(length)