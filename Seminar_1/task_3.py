# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def coordinatesCheck(x, y):
    if x==0 and y==0:
        return print("вы в начале координат")
    elif x!= 0 and y == 0:
        return print("вы на оси Y")
    elif x == 0 and y!=0:
        return print("вы на оси X")
    else:
        return quarter(x,y)



def quarter(x, y):
    if x > 0 and y > 0:
        print("Вы в ПЕРВОЙ четверти")
    elif x < 0 and y > 0:
        print("Вы во ВТОРО1 четверти")
    elif x < 0 and y < 0:
        print("Вы в ТРЕТЬЕЙ четверти")
    elif x > 0 and y < 0:
        print("Вы в ЧЕТВЕРТОЙ четверти")


x=int(input('введите координату x:\n'))
y=int(input('введите координату y:\n'))
coordinatesCheck(x,y)