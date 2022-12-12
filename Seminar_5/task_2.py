# Игра в конфеты


from random import *


welcome_text = ('Да начнутся конфетные игры!')
print(welcome_text)


def playerVsPlayer():
    totalSweets = int(input('На сколько кофнет будем играть?\n'))
    maxNum = 28
    count = 0
    firstPlayer = input('\nКто ты, Воин?\n ')
    secondPlayer = input('\nА этот справа кто?:\n')

    print('\nДля начала опеределим кто первый начнет игру.\n')

    x = randint(1, 2)
    if x == 1:
        lucky = firstPlayer
        loser = secondPlayer
    else:
        lucky = secondPlayer
        loser = firstPlayer
    print(f'Поздравляю {lucky} ты ходишь первым !')

    while totalSweets > 0:
        if count == 0:
            step = int(input(f'\nНу давай попробуем {lucky}\n'))
            if step > totalSweets or step > maxNum:
                step = int(input(f'\nНеее, ты что-то напутал {lucky}, можно взять только {maxNum} конфет. Давай по новой:\n'))
            totalSweets = totalSweets - step
        if totalSweets > 0:
            print(f'\nИтого у нас осталось {totalSweets}')
            count = 1
        else:
            print('Ну вот и все')

        if count == 1:
            step = int(input(f'\nСколько же выберет, как там его, {loser} '))
            if step > totalSweets or step > maxNum:
                step = int(input(f'\nНеее, ты что-то напутал {loser}, можно взять только {maxNum} конфет. Давай по новой:\n'))
            totalSweets = totalSweets - step
        if totalSweets > 0:
            print(f'\nИтого у нас осталось {totalSweets}')
            count = 0
        else:
            print('Пам-пам')

    if count == 1:
        print(f'{loser} ПОБЕДИЛ')
    if count == 0:
        print(f'{lucky} ПОБЕДИЛ')


def playerVsBot():
    totalSweets = int(input('На сколько кофнет будем играть?\n'))
    maxNum = 28
    firstPlayer = input('\nКто ты, Воин?\n ')
    secondPlayer = 'Компьютер'
    players = [firstPlayer, secondPlayer]
    print('\nДля начала опеределим кто первый начнет игру.\n')

    lucky = randint(0, 2)

    print(f'Поздравляю {players[lucky]} ты ходишь первым !')

    while totalSweets > 0:
        lucky += 1

        if players[lucky % 2] == 'Компьютер':
            print(f'\nХодит {players[lucky%2]}, конфет у нас {totalSweets}, сколько берете, мусье:\n')

            if totalSweets < 29:
                step = totalSweets
            else:
                delenie = totalSweets//28
                step = totalSweets - ((delenie*maxNum)+1)
                if step == -1:
                    step = maxNum -1
                if step == 0:
                    step = maxNum
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'\nХодит {players[lucky%2]}, конфет у нас {totalSweets}, сколько берете, сударь:\n'))
            while step > maxNum or step > totalSweets:
                step = int(input(f'\nЯ понимаю, что ты кантбитачт-кантбимувд, но за один ход можно взять {maxNum} конфет, давай летсгирит: '))
        totalSweets = totalSweets - step

    print(f'На кону осталось {totalSweets} \nПобедил {players[lucky%2]}')

chooseYourDestiny = int(input('Выбери, с кем хочешь сыграть:\n1 - с корешем\n2 - с ботом\n'))
if chooseYourDestiny == 1:
    playerVsPlayer()
elif chooseYourDestiny == 2:
    playerVsBot()
else:
    print('Я тебе чтоБ шутка какая-то?! Тут либо 1, либо 2. Третьего не дано')
    chooseYourDestiny = int(input('Выбери, с кем хочешь сыграть:\n1 - с корешем\n2 - с ботом\2'))
