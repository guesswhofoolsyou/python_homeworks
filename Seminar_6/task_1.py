# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.

def add_list():
    user_list = []
    num = int(input('Введите кол-во элементов списка: '))
    for i in range(0, num):
        user_list.append(input('Введите элемент списка: '))
    return user_list

def find_place(user_list):
    word = input('Введите искомый элемент: ')
    count = 0
    for i in range(0, len(user_list)):
        if word in user_list[i]:
            counter = i+1
            user_list[i] = 0
            count += 1
            if count == 2:
                break
    if count > 1:
        return f'позиция второго вхождения: {counter}'
    else:
        return 'нет второго вхождения'

user_list = add_list()
print (user_list)
print (find_place(user_list))
