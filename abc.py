import sys
import random

#Setting up Terminal Display, Seems clearer with underscores compared to dashes
def terminalDisplay():
    c=0
    for i in field[:2]:
        for j in i[:2]:
            print('', j, '|', end='')
        print('', field[c][2])
        c+=1
        print ('___________')
    print ('', field[2][0], '|', field[2][1], '|', field[2][2])

#Numbering from 1 to 9 on the grid
field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#Initial Interaction with the game
player = input('Player Name : ')
print('Welcome to Utkarsh\'s impossible Tic Tac Toe ', player)
terminalDisplay()
first = input('Do you want to move first: YES or NO? ')
print(str(first is "NO"))

#Making lists of all posible moves and win possiblities 
moveChoices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
winGame = [['1','2','3'], ['1','4','7'], ['1','5','9'], ['4','5','6'],['7','8','9'], ['2','5','8'],['3','6','9'],['3','5','7']]

firstAdvantage = ['5', '1', '3', '7', '9']

secondAdvantage = [['5', '1'], ['5', '3'], ['5', '7'],
                   ['5', '9'], ['1', '3'], ['3', '9'],
                   ['7', '9'], ['1', '7']]

thirdAdvantage = [['1', '3', '5'], ['3', '5', '9'], ['7', '5', '9'],
                  ['1', '5', '7'], ['1', '3', '9'], ['1', '3', '7'],
                  ['7', '9', '3'], ['2', '4', '1'], ['2', '3', '6'],
                  ['6', '9', '8'], ['4', '7', '8']]



moveCounter = 0
matchOver = False
userMoves = []
myMoves = []
if (first is "NO"):
    print ('My turn: ')

    if (len(moveChoices) > 0):
        myMove = think()

    if (myMove in moveChoices):
        moveChoices.remove(myMove)
    else:
        print ('Ah! I wanted to win.')

    populate(myMove, 'o')

    terminalDisplay()

    moveCounter += 1
'If player gets three in a row, player wins'
def checkWin(pos1, pos2, pos3, player):
    if ((pos1 is player) and (pos2 is player) and (pos3 is player)):
        playerWins = True
        draw = False
    else:
        playerWins = False
    return playerWins


'Check all possible win scenarios for a player.'
def checkWinner(player):
    for i in range(3):
        win = checkWin(field[i][0], field[i][1], field[i][2], player)
        if win:
            if player is 'o':
                print('Victory for me! told you, impossible ! ')
            else:
                print ('You won?! You are amazing!')
            draw = False
            sys.exit(0)
    for i in range(3):
        win = checkWin(field[0][i], field[1][i], field[2][i], player)
        if win:
            if player is 'o':
                print('Victory for me! told you, impossible ! ')
            else:
                print ('You won?! You are amazing!')
            draw = False
            sys.exit(0)
    win = checkWin(field[0][0], field[1][1], field[2][2], player)
    if win:
        if player is 'o':
            print('Victory for me! told you, impossible ! ')
        else:
            print ('You won?! You are amazing!')
        draw = False
        sys.exit(0)

    win = checkWin(field[0][2], field[1][1], field[2][0], player)
    if win:
        if player is 'o':
            print('Victory for me! old you, impossible ! ')
        else:
            print ('You won?! You are amazing!')
        draw = False
        sys.exit(0)
counter = 0
'Defines coordinates of each numbered position on board.'
def switch(x):
    return {
        '1': [0, 0],
        '2': [0, 1],
        '3': [0, 2],
        '4': [1, 0],
        '5': [1, 1],
        '6': [1, 2],
        '7': [2, 0],
        '8': [2, 1],
        '9': [2, 2]
    }[x]


'Fills a position with players move.'
def populate(x, side):
    nums = switch(x)
    field[nums[0]][nums[1]] = side


'Anticipate win or advantage for each player.'
def think():
    if moveCounter is 0:
        tInput = '5'
    elif moveCounter is 1:
        if userMoves[-1] is '5':
            tInput = '1'
        else:
            tInput = '5'
    else:
        tInput = anticipateWin()
    if tInput is '0':
        tInput = anticipateUserWin()
    if tInput is '0':
        tInput = anticipateAdvantage()
    if tInput is '0':
        tInput = anticipateUserAdvantage()
    if tInput is '0':
        tInput = random.choice(moves)
    myMoves.append(tInput)
    return tInput


def anticipate(posList, whoMoves):
    tInput = '0'
    for lis in posList:
        commonEl = set(whoMoves) & set(lis)
        if len(commonEl) > 1:
            for el in lis:
                if el not in commonEl:
                    if el in moveChoices:
                        tInput = el
                        break
                        break
    return tInput


def anticipateWin():
    tInput = anticipate(winGame, myMoves)
    return tInput


def anticipateUserWin():
    tInput = anticipate(winGame, userMoves)
    return tInput


def anticipateUserAdvantage():
    if len(userMoves) < 2:
        tInput = anticipate(secondAdvantage, userMoves)
    else:
        tInput = anticipate(thirdAdvantage, userMoves)
    return tInput


def anticipateAdvantage():
    tInput = '0'
    if len(myMoves) < 2:
        tInput = anticipate(secondAdvantage, myMoves)
    else:
        tInput = anticipate(thirdAdvantage, myMoves)
    return tInput




if (first is 'NO'):
    print ('My turn: ')

    if (len(moveChoices) > 0):
        myMove = think()

    if (myMove in moveChoices):
        moveChoices.remove(myMove)
    else:
        print ('Ah! I wanted to win.')

    populate(myMove, 'o')

    terminalDisplay()

    moveCounter += 1

draw = True

while (moveCounter < 9):

    move = input('Choose your move: ')

    userMoves.append(move)
    if (len(moveChoices) >= 0):
        moveChoices.remove(move)
    else:
        break

    populate(move, 'x')

    terminalDisplay()

    moveCounter += 1

    checkWinner('x')

    print ('My turn: ')

    if len(moveChoices) > 0:
        myMove = think()

    if (myMove in moveChoices):
        moveChoices.remove(myMove)
    else:
        print ('Ah! I wanted to win.')
        break

    populate(myMove, 'o')

    terminalDisplay()

    moveCounter += 1

    checkWinner('o')

if draw:
    print ('Draw')
else:
    print('Something\'s not right')
