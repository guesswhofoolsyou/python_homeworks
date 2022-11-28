# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = input("Укажите четверть для отображения  ")

quarterRangeX = {
    '1': " 0 < X < Infinity",
    '2': " -Infinity < X < 0",
    '3': " -Infinity < X < 0",
    '4': " 0 < X < Infinity"}
quarterRangeY = {
    '1': " 0 < Y < Infinity",
    '2': "  0 < Y < Infinity",
    '3': " -Infinity < Y < 0",
    '4': " -Infinity < Y < 0"}

print(quarterRangeX[quarter])
print(quarterRangeY[quarter])