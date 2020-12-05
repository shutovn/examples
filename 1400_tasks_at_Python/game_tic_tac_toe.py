"""
Игра крестики-нолики!
Для двух игроков, с размером поля 3х3

"""

# Импортируем фунцию random для случайного выбора игрока, который будет ходить первым.
import random
# Импортируем фунцию call для очистки дисплей в случае если игроки захотят сыграть еще раз.
from subprocess import call

player1_name = ''
player2_name = ''

def display_board(board):
    '''
    Функция отрисовывающая игровое поле.
    '''
    # Очищаем дисплей перед отрисовкой поля
    call("clear")
    # игровое поле
    print ("\t"," Крестики  Х ")
    print ("\t","-------------")
    print ("\t","|", board[1] ,"|", board[2] ,"|", board[3] ,"|","\t","Текущий ход за игроком: " + turn)
    print ("\t","-------------")
    print ("\t","|", board[4] ,"|", board[5] ,"|", board[6] ,"|","\t")
    print ("\t","-------------")
    print ("\t","|", board[7] ,"|", board[8] ,"|", board[9] ,"|","\t")
    print ("\t","-------------")
    print ("\t","  Нолики  0")

def player_name():
    global player1_name,player2_name
    player1_name = (input("Введите имя для первого игрока: "))
    player2_name = (input("Введите имя для второго игрока: "))

def player_input():

    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input(player1_name + ': Выберите себе маркер, X или O?').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):

    return ((board[7] == board[8] == board[9] == mark) or # across the top
    (board[4] == board[5] == board[6] == mark) or # across the middle
    (board[1] == board[2] == board[3] == mark) or # across the bottom
    (board[7] == board[4] == board[1] == mark) or # down the middle
    (board[8] == board[5] == board[2] == mark) or # down the middle
    (board[9] == board[6] == board[3] == mark) or # down the right side
    (board[7] == board[5] == board[3] == mark) or # diagonal
    (board[9] == board[5] == board[1] == mark)) # diagonal

def choose_first():
    if random.randint(0, 1) == 0:
        return player2_name
    else:
        return player1_name

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    #
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):

        position = input('Выберите следующую позицию: (1-9) ')
    return int(position)

def replay():
    return input('Хотите сыграть еще раз? Введите Yes или No: ').lower().startswith('y')

print('Добро пожаловать в игру Крестики - Нолики!')
print ("")
print ("\t","\\\\","","","","","","","","","//","","//","=","=","\\\\","","")
print ("\t","","\\\\","","","","","","","//","","//","","","","","","","\\\\",)
print ("\t","","","\\\\","","","","","//","","||","","","","","","","","","||",)
print ("\t","","","","\\\\","","","//","","","||","","","","","","","","","||",)
print ("\t","","","","","\\\\","//","","","","||","","","","","","","","","||",)
print ("\t","","","","","//","\\\\","","","","||","","","","","","","","","||",)
print ("\t","","","","//","","","\\\\","","","||","","","","","","","","","||",)
print ("\t","","","//","","","","","\\\\","","||","","","","","","","","","||",)
print ("\t","","//","","","","","","","\\\\","","\\\\","","","","","","","//",)
print ("\t","//","","","","","","","","","\\\\","","\\\\","=","=","//")
print ("")
player_name()

while True:
    # Сброс игрового поля и рандобмный выбор игрока начинающего игру.
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    game_on = True
    # Цикл самой игры!
    while game_on:

        if turn == player1_name:
            # Ход первого игрока.
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Поздравляем! Победа в этой битве за - ' + turn + '!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Эта партия закончилась Ничьей!')
                    break
                else:
                    turn = player2_name

        else:
            # Ход второго игрока.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Поздравляем! Победа в этой битве за - ' + turn + '!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Эта партия закончилась Ничьей!')
                    break
                else:
                    turn = player1_name

    if not replay():
        break
