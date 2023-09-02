# -*- coding: utf-8 -*-

import random, os, time

indexes = [str(i+1) for i in range(0,9)]

moves ={'1':'00','2':'01','3':'02','4':'10','5':'11','6':'12','7':'20','8':'21','9':'22'}

def login():
    print('Welcome to Tic Tac Toe')
    
    global gameBoard, playerName1, playerName2
    
    gameBoard = [['.','.','.'],
                ['.','.','.'],
                ['.','.','.']]
    
    state = True
    
    while state:
        playerName1 = input('please enter the first player\'s name: ').capitalize()
        print('')
        
        if playerName1 == '':
            print("Your player name can't be blank\n")
        elif len(playerName1) < 3:
            print('Your name needs to be longer than 2 characters.\n')
        else:
            print('Welcome', playerName1, 'Good Luck!')
            state = False
        
    state = True
    
    while state:
        playerName2 = input("Please Enter Second Player's Name: ").capitalize()
        print('')
        
        if playerName2 == "":
            print("Your Name Can't Be Blank")
        elif len(playerName2) < 3:
            print("Your Name Needs To Be More Than 2 Characters Long.\n")
        elif playerName2 == playerName1:
            print(playerName1, "is taken, please choose another name.")
        else:
            print('Welcome', playerName2, 'Good Luck!')
            state = False
    
    prepareForGame(playerName1, playerName2)

def prepareForGame(firstPlayer, secondPlayer):
    print('Now I will decide who goes first and who plays as what')
    
    firstPlayerShape, secondPlayerShape = random.sample(['X', 'O'], 2)
    
    print(firstPlayer, 'goes first and plays as', firstPlayerShape)
    print(secondPlayer, 'is second and plays as', secondPlayerShape)
    time.sleep(3)
    
    players = {firstPlayer: firstPlayerShape, secondPlayer: secondPlayerShape}
    
    gameLogic(firstPlayer, secondPlayer, players)

def gameLogic(firstPlayer, secondPlayer, players):
    gameBoard = [['.' for _ in range(3)] for _ in range(3)]
    indexes = [str(i+1) for i in range(9)]
    moves = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
             '4': (1, 0), '5': (1, 1), '6': (1, 2),
             '7': (2, 0), '8': (2, 1), '9': (2, 2)}
    
    def print_board():
        for row in gameBoard:
            print(' '.join(row))
    
    def check_winner(player):
        for i in range(3):
            if all(gameBoard[i][j] == player for j in range(3)):
                return True
            if all(gameBoard[j][i] == player for j in range(3)):
                return True
        if all(gameBoard[i][i] == player for i in range(3)) or all(gameBoard[i][2-i] == player for i in range(3)):
            return True
        return False
    
    turn = 0
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board()
        
        if turn % 2 == 0:
            name = firstPlayer
        else:
            name = secondPlayer
        
        print('It is your turn,', name)
        index = input('Please choose an index (1-9): ')
        
        if index not in indexes:
            print('Please enter a valid index (1-9)')
        else:
            row, col = moves[index]
            if gameBoard[row][col] == '.':
                gameBoard[row][col] = players[name]
                if check_winner(players[name]):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_board()
                    print('Congratulations,', name, 'you won.')
                    print('Game is over')
                    break
                elif '.' not in ''.join([''.join(row) for row in gameBoard]):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_board()
                    print("It's a draw!")
                    print('Game is over')
                    break
                turn += 1

    while True:
        again = input('Do you want to play again (y or n)?: ')
        if again == 'y':
            login()
        elif again == 'n':
            print('Thank you for playing. I hope I can see you soon! :)')
            exit()
        else:
            print("Your answer can only be 'y' or 'n'. Please enter a valid answer.")

if __name__ == '__main__':
    login()


        
                    
                    
            
            








            