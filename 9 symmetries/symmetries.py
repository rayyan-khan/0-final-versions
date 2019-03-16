import sys

# import one or two arguments
# if one: that is the matrix (as a string)
# if two: first is matrix (as a string),
# second is its width
board = ''
width = 0
if len(sys.argv) == 2:
    board = sys.argv[1]
elif len(sys.argv) == 3:
    board = sys.argv[1]
    width = int(sys.argv[2])


# helper methods
def printMatr(matr, w = 0):
    # given an array of arrays or a string (and width
    # of the array it represents) print it out
    if w:
        for index in range(len(matr)):  # matr is a string in this case
            if index % w == 0:  # left side
                print('{} '.format(matr[index]), end='')
            elif index % w == w - 1:  # right side
                print('{}\n'.format(matr[index]), end='')
            else:
                print(' {} '.format(matr[index]), end='')
    else:
        for row in range(len(matr)):
            print(' '.join([str(i) for i in matr[row]]))


def matrToString(matr):
    # given an array of arrays, return a string of
    # its contents starting top left to bottom right
    s = ''
    for row in range(len(matr)):
       s += ''.join([str(i) for i in matr[row]])
    return s


def detWidth(s):
    # based on string representing matrix,
    # determine its width: smallest integer
    # that evenly divides the length of the
    # board that is no less than the square
    # root of the length of the board
    s = len(s)
    i = 1
    if s**.5 == (s**.5)//1:
        return int(s**.5)
    while True:
        possW = int((s**.5)//1 + i)
        if s % possW == 0:
            return possW
        i += 1


def strToMatr(smatr, w):
    matr = []
    for r in range(int(len(smatr)/w)):
        row = []
        for col in range(w):
            row.append(smatr[r*w + col])
        matr.append(row)
    return matr


# rotations
def rotateCCW(matr):
    w = len(matr[0])
    newmatr = [[0 for i in range(len(matr))] for j in range(w)]
    for row in range(len(matr)):
        for col in range(w):
            newmatr[w - col - 1][row] = matr[row][col]
    return newmatr


def rotate180(matr): # probably not efficient, but whatever
    ccwmatr = rotateCCW(matr)
    return rotateCCW(ccwmatr)


def rotateCW(matr):
    matr180 = rotate180(matr)
    return rotateCCW(matr180)


# reflections
def flipV(matr):
    w = len(matr[0])
    newmatr = [[0 for i in range(w)] for j in range(len(matr))]
    for row in range(len(matr)):
        for col in range(w):
            newmatr[row][w - col - 1] = matr[row][col]
    return newmatr


def flipH(matr):
    w = len(matr[0])
    h = len(matr)
    newmatr = [[0 for i in range(w)] for j in range(len(matr))]
    for row in range(h):
        for col in range(w):
            newmatr[h - row - 1][col] = matr[row][col]
    return newmatr


def flipPosDiag(matr):
    ccwm = rotateCCW(matr)
    return flipV(ccwm)


def flipNegDiag(matr):
    ccwm = rotateCCW(matr)
    return flipH(ccwm)


# run:
syms = set()
if width == 0:
    width = detWidth(board)
matr = strToMatr(board, width)

syms.add(board)
syms.add(matrToString(rotateCCW(matr)))
syms.add(matrToString(rotate180(matr)))
syms.add(matrToString(rotateCW(matr)))
syms.add(matrToString(flipV(matr)))
syms.add(matrToString(flipH(matr)))
syms.add(matrToString(flipPosDiag(matr)))
syms.add(matrToString(flipNegDiag(matr)))

for sym in syms:
    print(sym)
