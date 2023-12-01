bräda = [' ' for x in range(10)]

def insertLetter(bokstav,pos):
    bräda[pos] = bokstav

def spaceIsFree(pos):
    return bräda[pos] == ' '

def printBoard(bräda):
    print('   |   |   ')
    print(' ' + bräda[1] + ' | ' + bräda[2] + ' | ' + bräda[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + bräda[4] + ' | ' + bräda[5] + ' | ' + bräda[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + bräda[7] + ' | ' + bräda[8] + ' | ' + bräda[9])
    print('   |   |   ')

def isBoardFull(bräda):
    if bräda.count(' ') > 1:
        return False
    else:
        return True

def IsWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))
def playerMove():
    run = True
    while run:
        move = input("Snälla välj en position att lägga X mellan 1 och 9\n")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X' , move)
                else:
                    print('Nononono redan occuperad')
            else:
                print('var vänlig och skriv ett nummer mellan 1 och 9')

        except:
            print('Snälla skriv ett nummer')

def computerMove():
    possibleMoves = [x for x , letter in enumerate(bräda) if letter == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            brädacopy = bräda[:]
            brädacopy[i] = let
            if IsWinner(brädacopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Välkommen till spelet!")
    printBoard(bräda)

    while not(isBoardFull(bräda)):
        if not(IsWinner(bräda , 'O')):
            playerMove()
            printBoard(bräda)
        else:
            print("Du förlorade!")
            break

        if not(IsWinner(bräda , 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertLetter('O' , move)
                print('datorn la en o på position' , move , ':')
                printBoard(bräda)
        else:
            print("Du vann!")
            break




    if isBoardFull(bräda):
        print("Ingen vinnare")

while True:
    x = input("Vill du spela? Skriv y för ja och n nej no (y/n)\n")
    if x.lower() == 'y':
        bräda = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
