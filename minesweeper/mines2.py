"""Round 2 of Minesweeper for Decision-Making"""

import random, time, copy

name = input("Name: ")
trial_type = input("Trial Type (Practice/Test)?: ")
trial_num = input("Trial number: ")
outputFile = open(name + "_mine2" + "_" + trial_type + trial_num + '.txt', 'w+')

def reset(): # reset game
    print(open('instructions2.txt', 'r').read())
    input("Press [enter] when ready to play")
    b = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    for n in range(0, 10):
        placeBomb(b)
    for r in range(0, 6):
        for c in range (0, 6):
            value = l(r, c, b)
            if value == "*":
                updateValues(r,c,b)
    #print(b)
    k = [[' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ']]
    printBoard(k)
    startTime = time.time() # start timer
    play(b, k, startTime)

def placeBomb(b):
    r = random.randint(0,5)
    c = random.randint(0,5)
    if not b[r][c] == '*':
        b[r][c] = '*'
    else:
        placeBomb(b)

def l(r, c, b): # location
    return b[r][c]

def updateValues (rn,c,b):
    if rn-1 > -1:
        r = b[rn-1]

        if c-1 > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if not r[c] == '*':
            r[c] += 1

        if 6 > c+1:
            if not r[c+1] == '*':
                r[c+1] += 1
    r = b[rn]

    if c-1 > -1:
        if not r[c-1] == '*':
            r[c-1] += 1

    if 6 > c+1:
        if not r[c+1] == '*':
            r[c+1] += 1

    if 6 > rn+1:
        r = b[rn+1]

        if c-1 > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if not r[c] == '*':
            r[c] += 1

        if 6 > c+1:
            if not r[c+1] == '*':
                r[c+1] += 1

def printBoard(b):
    for n in range (0, 5): # print blank lines
        print()

    print('    A   B   C   D   E   F')
    print('  ╔═══╦═══╦═══╦═══╦═══╦═══╗')

    for r in range (0, 6):
        print(r,'║',l(r,0,b),'║',l(r,1,b),'║',l(r,2,b),'║',l(r,3,b),'║',l(r,4,b),'║',l(r,5,b),'║')
        if not r == 5:
            print('  ╠═══╬═══╬═══╬═══╬═══╬═══╣')

    print('  ╚═══╩═══╩═══╩═══╩═══╩═══╝')

def play (b, k, startTime):
    c, r = choose (b, k, startTime)
    v = l(r, c, b) # get value of the square chosen by the player
    if v == "*": # chosen square is a bomb
        printBoard(b)
        score = FindScore(b, k)
        print ('You lose!')
        print ('Time taken: ' + str(round(time.time() - startTime)) + ' sec')
        print ('Score:', score)
        outputFile.write('Time taken: ' + str(round(time.time() - startTime)) + ' sec')
        outputFile.write('\nScore: ' + str(score))
        exit()

    k[r][c] = v #put value uncovered by player in the known grid

    if v == 0:
        checkZeros(k, b, r, c) # open all zeros around the chosen square
    printBoard(k)

    # start change here
    if v != 0 and v != "*":
        DiagonalMines = CheckDiagonal(r, c, b)
        if DiagonalMines == 1:
            print('Mine in diagonal position?: Yes\n')
        elif DiagonalMines == 0:
            print('Mine in diagonal position?: No\n')

    squaresLeft = 0
    for x in range(0,6):
        row = k[x]
        squaresLeft += row.count(' ')
        squaresLeft += row.count('⚐')

    if squaresLeft == 10:
        printBoard(b)
        print('You win!')
        print ('Time taken: ' + str(round(time.time() - startTime)) + ' sec')
        outputFile.write('Time taken: ' + str(round(time.time() - startTime)) + ' sec')
        outputFile.write('\nScore: 10')
        exit()

    play(b, k, startTime)

def choose(b, k, startTime):
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    numbers = ['0', '1', '2', '3', '4', '5']

    while True:
        chosen = input('Choose a square (eg. E4) or place a marker (eg. mE4): ').lower()
        if len(chosen) == 3 and chosen[0] == 'm' and chosen[1] in letters and chosen[2] in numbers:
            c, r = (ord(chosen[1]))-97, int(chosen[2])
            marker(r, c, k)
            play(b, k, startTime)
            break

        elif len(chosen) == 2 and chosen[0] in letters and chosen[1] in numbers:
            return (ord(chosen[0]))-97, int(chosen[1])

        else:
            choose(b, k, startTime)

def marker(r, c, k):
    k[r][c] = '⚐'
    printBoard(k)

def checkZeros(k, b, r, c):
    oldGrid = copy.deepcopy(k)
    zeroProcedure(r, c, k, b)
    if oldGrid == k:
        return
    while True:
        oldGrid = copy.deepcopy(k)
        for x in range (6):
            for y in range (6):
                if l(x, y, k) == 0:
                    zeroProcedure(x, y, k, b)
        if oldGrid == k:
            return

def zeroProcedure(r, c, k, b):
    if r-1 > -1: #Row above
        row = k[r-1]
        if c-1 > -1: row[c-1] = l(r-1, c-1, b)
        row[c] = l(r-1, c, b)
        if 6 > c+1: row[c+1] = l(r-1, c+1, b)

    #Same row
    row = k[r]
    if c-1 > -1: row[c-1] = l(r, c-1, b)
    if 6 > c+1: row[c+1] = l(r, c+1, b)

    #Row below
    if 6 > r+1:
        row = k[r+1]
        if c-1 > -1: row[c-1] = l(r+1, c-1, b)
        row[c] = l(r+1, c, b)
        if 6 > c+1: row[c+1] = l(r+1, c+1, b)

def CheckDiagonal(r, c, b):
    DiagonalMines = 0
    if r == 0: # first row, don't check r - 1
        if c == 0 and b[r+1][c+1] == "*":
            DiagonalMines = 1
        elif c == 5 and b[r+1][c-1] == "*":
            DiagonalMines = 1
        elif c != 0 and c != 5:
            if b[r+1][c-1] == "*" or b[r+1][c+1] == "*":
                DiagonalMines = 1
        else:
            pass

    elif r == 5: # last row, don't check r + 1
        if c == 0 and b[r-1][c+1] == "*":
            DiagonalMines = 1
        elif c == 5 and b[r-1][c-1] == "*":
            DiagonalMines = 1
        elif c != 0 and c != 5:
            if b[r-1][c-1] == "*" or b[r-1][c+1] == "*":
                DiagonalMines = 1
        else:
            pass

    else: # middle rows, check above and below
        if c == 0 and (b[r-1][c+1] == "*" or b[r+1][c+1] == "*"):
            DiagonalMines = 1
        elif c == 5 and (b[r-1][c-1] == "*" or b[r+1][c-1] == "*"):
            DiagonalMines = 1
        elif c != 0 and c != 5:
            if b[r-1][c-1] == "*" or b[r-1][c+1] == "*" or b[r+1][c-1] == "*" or b[r+1][c+1] == "*":
                DiagonalMines = 1
        else:
            pass

    return DiagonalMines

def FindScore(b, k):
    score = 0
    for r in range (0,6):
        for c in range (0,6):
            if k[r][c] == "⚐" and b[r][c] == "*":
                score += 1

    return score

print()
print('Welcome to Minesweeper!')
print('=========================')
reset()
