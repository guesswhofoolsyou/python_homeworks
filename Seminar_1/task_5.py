# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

firstPoint = list(input("Введите координаты первой точки через пробел:\n").split())
secondPoint = list(input("Введите координаты первой точки через пробел:\n").split())
print(firstPoint)
print(secondPoint)


def distance(firstPoint, secondPoint):
    if len(firstPoint) != len(secondPoint):
        print("Точки в разных измерениях")
    else:
        dist = float(0)
        for i in range(len(firstPoint)):
            dist += (int(secondPoint[i])-int(firstPoint[i]))**2
        print(f"Прямое расстояние между точками {round(dist**(1/2),2)}")


distance(firstPoint, secondPoint)