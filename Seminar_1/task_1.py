# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def weekend():
    day = int(input("впишите день недели :\n"))
    if day == 6 or day == 7:
        print(f"{day} -> да")
    elif 0 < day < 6:
        print(f"{day} -> нет")
    else:
        print(f"{day} -> введен не день недели")
        weekend()

weekend()