'''
 sudoku final due 11-28-18
 not my best, was really tired this week
 a) didn't comment well, just tried to make things work until they did
 b) kind of messy/disorganized in general
 c) only down to 30s rather than 10s
 d) note to self if I'm reading this in the future: 
    you can probably think about improving this by finding not only the best 
    position, but also the best symbol to put in that position (e.g. in the dict 
    with the keys as positions and symbols as possible placements -- kind of the 
    opposite of that -- the best symbol has the fewest corresponding positions). 
    If you don't do it efficiently, though, it'll just slow things down. 
    Besides that, I'd definitely look at the getBestPos method because...yeah. 
    Maybe even how newIndSyms is created but unsure about whether that'd break 
    things. 
 - 12-3-18
'''

import sys
import time

# input:
INPUT = open(sys.argv[1], 'r') if len(sys.argv) == 2 else open('puzzles.txt', 'r')

# set up global variables:
INP = '.' * 81

# just for self-reference:
'''
NBRS = {index: {neighboring indexes}}
INDSYM = {index: {possible symbols}}
CSTRSIZE = size of constraint
SYMSET = possible symbols
'''

def setGlobals(pzl):
    global PZLSIZE, CSTRSIZE, CSTRS, SYMSET, NBRS

    pzl = ''.join([n for n in pzl if n != '.'])

    PZLSIZE = len(INP)
    CSTRSIZE = int(len(INP) ** .5)
    subheight, subwidth = int(CSTRSIZE ** .5), int(CSTRSIZE ** .5) \
        if int(CSTRSIZE ** .5 // 1) == int(CSTRSIZE ** .5) \
        else (int(CSTRSIZE ** .5 // 1), int(CSTRSIZE ** .5 // 1 + 1))

    SYMSET = {n for n in pzl} - {'.'}
    if len(SYMSET) != CSTRSIZE:
        otherSyms = [n for n in '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0']
        while len(SYMSET) < CSTRSIZE:
            SYMSET.add(otherSyms.pop(0))

    rowcstr = [{index for index in range(row * CSTRSIZE, (row + 1) * CSTRSIZE)}
               for row in range(CSTRSIZE)]
    colcstr = [{index for index in range(col, col + PZLSIZE - subwidth * subheight + 1, subwidth * subheight)}
               for col in range(CSTRSIZE)]
    subcstr = [{boxRow + boxColOffset + subRow * CSTRSIZE + subCol
                for subRow in range(subheight) for subCol in range(subwidth)}
               for boxRow in range(0, PZLSIZE, subheight * CSTRSIZE) for boxColOffset in range(0, CSTRSIZE, subwidth)]
    CSTRS = rowcstr + colcstr + subcstr
    NBRS = [set().union(*[cset for cset in CSTRS if n in cset]) - {n} for n in range(PZLSIZE)]
    indsym0 = {index: SYMSET - {INP[n] for n in NBRS[index]} for index in range(PZLSIZE) if INP[index] == '.'}
    return indsym0


# helper methods
def printPzl(pzl):
    cstrsize = int(len(pzl) ** .5)
    subheight, subwidth = int(cstrsize ** .5), int(cstrsize ** .5) \
        if int(cstrsize ** .5 // 1) == int(cstrsize ** .5) \
        else (int(cstrsize ** .5 // 1), int(cstrsize ** .5 // 1 + 1))
    rowLen = subwidth * (int(cstrsize / subheight))
    for row in range(cstrsize):
        print(' '.join(pzl[rowLen * row: rowLen * (row + 1)]))


def checkSum(pzl):
    return sum(ord(n) for n in pzl) - PZLSIZE * ord('0')

def getBestPos(indSyms):
    mostConstrained = CSTRSIZE  # number of syms already placed in NBRS[index] -- larger = fewer options
    bestPos = set()
    for pos in indSyms:  # for each unfilled position in pzl
        numSyms = len(indSyms[pos])  # find the number of syms placed
        if numSyms < mostConstrained:  # if its bigger than the current biggest
            mostConstrained = numSyms  # set it as the biggest
            bestPos = set()  # and reset bestPos
            bestPos.add(pos)
    return bestPos

def updateIndSym(updatedInd, sym, indSyms, pzl):
    for nbr in NBRS[updatedInd]:
        if nbr in indSyms:
            indSyms[nbr] = indSyms[nbr] - {sym}
    print('updated index', indSyms.pop(updatedInd), updatedInd)  # remove as possible
    return indSyms


# solve
def solve(pzl, indSyms):
    if pzl.find('.') == -1 or not indSyms:
        return pzl

    bestPos = getBestPos(indSyms)

    for pos in bestPos:
        for sym in indSyms[pos]:
            newIndSyms = {pos: {s for s in indSyms[pos]} for pos in indSyms}
            for nbr in NBRS[pos]:
                if nbr not in indSyms and pzl[nbr] == sym:
                    continue
                if nbr in indSyms:
                    newIndSyms[nbr].discard(sym)
            del newIndSyms[pos]
            pzlMove = pzl[:pos] + sym + pzl[pos + 1:]
            newPzl = solve(pzlMove, newIndSyms)
            if newPzl:
                return newPzl
    return ''


# run
time51 = time.clock()
totalTime = time.clock()
for line in enumerate(INPUT.readlines()):
    start = time.clock()
    pzlNum, INP = line
    if pzlNum == 127:
        print('Puzzle:', pzlNum + 1, '\nOriginal:', line[1])
    print('Puzzle:', pzlNum + 1, '\nOriginal:', line[1], end='')
    INP = INP.strip()
    indsym1 = setGlobals(INP)
    solution = solve(INP, indsym1)
    if pzlNum == 50:
        print('TIME FOR 51: {} seconds'.format(time.clock() - time51))
    print('Solution: {} \nTime: {} Sum: {} \n'.format(solution, round(time.clock() - start, 3), checkSum(solution)),
          end='')
    if solution == '':
        print('No solution -- i.e. theres a bug here on puzzle', pzlNum)
print('TOTAL TIME:', round(time.clock() - totalTime, 3))
