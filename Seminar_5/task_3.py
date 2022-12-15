# "Крестики-нолики"

import random

def choosePlayer():
    firstPlayer = []
    secondPlayer = []
    firstPlayerName = input('\nКто ты, Воин?\n ')
    secondPlayerName = input('\nА этот справа кто?:\n')
    firstPlayer.append(firstPlayerName)
    secondPlayer.append(secondPlayerName)
    token = ['X', 'O']

    print('\nДля начала опеределим кто первый начнет игру.\n')

    x = random.randint(1, 2)
    if x == 1:
        print(f'Поздравляю {firstPlayer[0]} ты ходишь {token[0]}!')
        firstPlayer.append(token[0])
        secondPlayer.append(token[1])
        playerName = [firstPlayer, secondPlayer]
    else:
        print(f'Поздравляю {secondPlayer[0]} ты ходишь {token[0]}!')
        secondPlayer.append(token[0])
        firstPlayer.append(token[1])
        playerName = [secondPlayer, firstPlayer]
    return playerName

def drawBoard (board):
    print ("-------------")
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-------------")
    return board

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def game(token):
    valid = False
    while not valid:
        playerAnswer = input("Куда поставим " + token +"? ")
        try:
            playerAnswer = int(playerAnswer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if playerAnswer >= 1 and playerAnswer <= 9:
            if (str(board[playerAnswer-1]) not in "XO"):
                board[playerAnswer-1] = token
                valid = True
            else:
                print ("Эта клетка уже занята")
        else:
            print ("ЭМ АЙ Э ДЖУК ФО Ю??? Введите число от 1 до 9 чтобы совершить ход.")

def main():
    counter = 0
    win = False
    while not win:
        drawBoard(board)
        if counter % 2 == 0:
            game(playerName[0][1])
        else:
            game(playerName[1][1])
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                if playerName[0][1] == tmp:
                    print (playerName[0][0], "выиграл!")
                    win = True
                    break
                else:
                    print (playerName[1][0], "выиграл!")
                    win = True
                    break
        if counter == 9:
            print ("Ничья!")
            break
    drawBoard(board)

board = list(range(1,10))
playerName = choosePlayer()
main()


# board = list(range(1,10))

# def draw_board(board):
#     print ("-" * 13)
#     for i in range(3):
#         print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print ("-" * 13)

# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token+"? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print ("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer-1]) not in "XO"):
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print ("Эта клеточка уже занята")
#         else:
#             print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

# def check_win(board):
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print (tmp, "выиграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print ("Ничья!")
#             break
#     draw_board(board)

# main(board)