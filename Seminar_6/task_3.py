# Сформировать список из N членов последовательности.

def add_list():
    user_list = [1]
    while True:
        try:
            num = int(input('Введите кол-во элементов списка: '))
        except ValueError:
                print('Это не число. Давай по новой.')
        else:
            break
    for i in range (1, num):
        user_list.append(user_list[i-1]*-3)
    return user_list

user_list = add_list()
print (user_list)