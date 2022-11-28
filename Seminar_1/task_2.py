# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"

def logicCheck(X, Y, Z):
    firstHalf = X or Y or Z
    secondHalf = not X and not Y and not Z
    check = not firstHalf == secondHalf
    print(check)

firstStatement = input("Первая предиката = ")
secondStatement = input("Вторая предмката = ")
thirdStatement = input("Тертья предиката = ")

logicCheck(firstStatement, secondStatement, thirdStatement)