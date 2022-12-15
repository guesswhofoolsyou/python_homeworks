# Найти произведение пар чисел в списке.

def add_list():
    user_list = []
    num = int(input('Введите кол-во элементов списка: '))
    while True:
        try:
            for i in range(0, num):
                user_list.append(int(input('Введите число: ')))
        except ValueError:
                print('Это не число. Давай по новой.')
                user_list = []
        else:
            break
    return user_list

def multiply(user_list):
    multiply_list = []
    if len(user_list)%2 !=0:
        for i in range (0, len(user_list)//2):
            multiply_list.append(user_list[i]*user_list[len(user_list)-i-1])
        multiply_list.append(user_list[len(user_list)//2]**2)
    else:
        for i in range (0, len(user_list)//2):
            multiply_list.append(user_list[i]*user_list[len(user_list)-i-1])
    return multiply_list

user_list = add_list()
print (user_list)
print (multiply(user_list))
