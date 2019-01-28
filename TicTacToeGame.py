def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    
    while True:
        playerInput = input('Would you like to be "X" or "O"?')
        playerInput = playerInput.upper()
        if playerInput != 'X' and playerInput != 'O':
            continue
        else:
            print('Ok. You will be '+ playerInput)
            return playerInput

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    #All possible winning combinations:
    return (board[1] == mark and board[2] == mark and board[3] == mark) or\
    (board[4] == mark and board[5] == mark and board[6] == mark) or\
    (board[7] == mark and board[8] == mark and board[9] == mark) or\
    (board[1] == mark and board[4] == mark and board[7] == mark) or\
    (board[2] == mark and board[5] == mark and board[8] == mark) or\
    (board[3] == mark and board[6] == mark and board[9] == mark) or\
    (board[1] == mark and board[5] == mark and board[9] == mark) or\
    (board[3] == mark and board[5] == mark and board[7] == mark)

import random

def choose_first():
    playerGoesFirst = random.randint(1,2)
    print('Player ' + str(playerGoesFirst) + ' goes first')
    return playerGoesFirst

def space_check(board, position):
    position = int(position)
    return board[position] == ' '

def full_board_check(board):
    return not(' ' in board[1:10])

def player_choice(board):
    numbers = ['1','2','3','4','5','6','7','8','9']
    while True:
        playerChoice = input('Please choose a position from 1-9: ')
        if not(playerChoice in numbers):
            print('Error! Please try again.')
            continue
        else:
            if space_check(board,playerChoice):
                return int(playerChoice)
            else:
                print('Oops! That space is already occupied. Please try again')
                continue

def replay():
    while True:
        playAgainOption = input('Would you like to play again? Enter Y or N: ')
        playAgainOption = playAgainOption.lower()
        if playAgainOption == 'y':
            print('\n')
            return True
        elif playAgainOption == 'n':
            print('Thanks for playing!')
            return False
        else:
            continue

# The Game!

print('Welcome to Tic Tac Toe!\n')

while True:
    #Game Setup
    gameBoard = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(gameBoard)
    print('\n')
    firstPlayer = choose_first()
    
    if firstPlayer == 1:
        secondPlayer = 2
    else:
        secondPlayer = 1
    
    firstPlayerChoice = player_input()
    
    if firstPlayerChoice == 'X':
        secondPlayerChoice = 'O'
    else:
        secondPlayerChoice = 'X'
        
    while True:
        #Player 1's turn
        print('Player ' + str(firstPlayer) + ':\n')
        place_marker(gameBoard,firstPlayerChoice,player_choice(gameBoard))
        display_board(gameBoard)
        if win_check(gameBoard,firstPlayerChoice):
            print('Player ' + str(firstPlayer) + ' wins!')
            break
        if full_board_check(gameBoard):
            print('Draw 1/2 - 1/2 Anish Giri')
            break
        #Player 2's turn
        print('Player ' + str(secondPlayer) + ':\n')
        place_marker(gameBoard,secondPlayerChoice,player_choice(gameBoard))
        display_board(gameBoard)
        if win_check(gameBoard,secondPlayerChoice):
            print('Player ' + str(secondPlayer) + ' wins!')
            break
            
    if replay():
        continue
    else:
        break