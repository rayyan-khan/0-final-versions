'''
A-star for 15-puzzle, to turn in Friday, 10/26.

Goal is to run the puzzles 'eckel.txt' in as little time as possible. 
This takes about 10 minutes, which was about half the class average
and earned a grade of 96.25%. 

It opens a file specified from the command line (with a default of
'eckel.txt'). It takes the first puzzle as the goal state for all
the following puzzles, and then outputs the puzzle, puzzle number,
time to solve the puzzle, and sequence of indices the "space" moves
to in order for the puzzle to match the goal state. 
'''

import time
import sys
import heapq


# either sys input of a file or eckel.txt
FILE = open(sys.argv[1], 'r') if len(sys.argv) == 2 else open('eckel.txt', 'r')

# puzzle/goal related variables:
GOAL = FILE.readline().strip()  # goal is first puzzle in the file
if '0' in GOAL:  # if it's one of eckel's puzzles, switch to ours
    GOAL = GOAL[0:GOAL.find('0')].lower() + '_' + GOAL[GOAL.find('0') + 1:].lower()
PZLSIZE = len(GOAL)  # the size/length of the input puzzles
SIDELEN = int(PZLSIZE**.5)  # the side length of the input puzzles
GOALSPACE = GOAL.find('_')  # the index of the space in the goal
GOALINDEXES = {k[1]: k[0] for k in enumerate(GOAL)}  # GOALINDEXES = {letter: index}

# create LOOKUPNBRS to find the possible moves from a given space index:
LOOKUPNBRS = [[] for i in range(PZLSIZE)]
# corners
LOOKUPNBRS[0] = [1, SIDELEN]  # top left
LOOKUPNBRS[SIDELEN - 1] = [SIDELEN - 2, SIDELEN * 2 - 1]  # top right
LOOKUPNBRS[PZLSIZE - SIDELEN] = [PZLSIZE - SIDELEN + 1, PZLSIZE - 2 * SIDELEN]  # bottom left
LOOKUPNBRS[PZLSIZE - 1] = [PZLSIZE - 2, PZLSIZE - SIDELEN - 1]  # bottom right
for n in range(PZLSIZE):
    if not LOOKUPNBRS[n]:  # if not empty
        # edges
        if n < SIDELEN:  # top edge
            LOOKUPNBRS[n] = [n - 1, n + SIDELEN, n + 1]
        elif n > PZLSIZE - SIDELEN:  # bottom edge
            LOOKUPNBRS[n] = [n - 1, n + 1, n - SIDELEN]
        elif n % SIDELEN == 0:  # left edge
            LOOKUPNBRS[n] = [n + SIDELEN, n + 1, n - SIDELEN]
        elif n % SIDELEN == SIDELEN - 1:  # right edge
            LOOKUPNBRS[n] = [n - SIDELEN, n - 1, n + SIDELEN]
        else:  # center (has four neighbors)
            LOOKUPNBRS[n] = [n - SIDELEN, n - 1, n + SIDELEN, n + 1]

# manhattan distance related variables:
# COORDINATES for manhattan distances, top left being (0,0)
COORDINATES = [(k % SIDELEN, k // SIDELEN) for k in range(PZLSIZE)]

def getMnht(from_, to_):
    # dict Δx + Δy for one swap
    return abs((COORDINATES[from_][0]) - (COORDINATES[to_][0])) \
           + (abs((COORDINATES[from_][1]) - (COORDINATES[to_][1])))

MNHTCOORDINATES = {(from_, to_): getMnht(from_, to_)
                   for to_ in range(PZLSIZE) for from_ in range(PZLSIZE)}

# UPDATEMNHT= {(from, to): +- 1} --> (+) if mnht dist increases, (-) if decreases
# don't have to calculate mnhtPuzzle for each puzzle anymore, saving time
UPDATEMNHT = {}
for from_ in range(PZLSIZE):
    for to_ in LOOKUPNBRS[from_]:
        for ch in GOAL:
            if ch != '_':
                if MNHTCOORDINATES[(to_, GOALINDEXES[ch])] \
                        > MNHTCOORDINATES[(from_, GOALINDEXES[ch])]:
                    UPDATEMNHT[(from_, to_, ch)] = -1
                else:
                    UPDATEMNHT[(from_, to_, ch)] = 1


# helper methods:

def solvable(puzzle, GOAL='_abcdefghijklmno'):
    # is the puzzle solvable for the given goal state? returns true/false

    inversions = len([item for sublist in
                      [[k for k in puzzle[puzzle.find(n) + 1:]
                        if k != '_' and n > k] for n in puzzle if n != '_']
                      for item in sublist])

    if SIDELEN % 2 == 0: # have to account for rows in even sided puzzles
        rowDifference = (puzzle.find('_') // SIDELEN - GOAL.find('_') // SIDELEN)
        return rowDifference % 2 == inversions % 2
    return inversions % 2 == 0


def mnhtPuzzle(puzzle, GOAL = '_abcdefghijklmno'):
    # returns the manhattan distance for the entire puzzle
    # by adding them up index by index
    return sum([MNHTCOORDINATES[index, GOALINDEXES[ch]]
                for index, ch in enumerate(puzzle) if ch != '_'])


def swapChars(num, space, puzzle): # space = to_, num = from_
    # returns a string with the space and character in the neighboring index swapped
    if num < space:
        return puzzle[0:num] + '_' + puzzle[num + 1: space] + puzzle[num] + puzzle[space + 1:]
    return puzzle[0:space] + puzzle[num] + puzzle[space + 1: num] + '_' + puzzle[num + 1:]


def neighbors(puzzle, space):
    # returns a list containing (nbr puzzle, new space) for each possible neighbor
    return [(swapChars(num, space, puzzle), num) for num in LOOKUPNBRS[space]]
    # change is to store location of the space in a tuple with the neighbor so we don't need .find


def updateEst(from_, to_, ch, est):
    # updates est by 0 or 2 depending on whether mnhtDist goes up or down
    if UPDATEMNHT[(from_, to_, ch)] == -1:
        return est
    return est + 2


def getPath(nbr, lvl, closedSet):
    # called when goal is found in astar, returns list of puzzles back to start
    pathList=[nbr]
    while lvl != 0:
        for n in neighbors(nbr, nbr.find('_')):
            nPzl = n[0]  # neighbors returns a list like
                         # [(neighbor puzzle, space location)]
            if nPzl in closedSet and closedSet[nPzl] == lvl - 1:
                nbr, lvl = nPzl, closedSet[nPzl]
                pathList.insert(0, nPzl)
    return pathList


# A-STAR
def solve(puzzle, goal='_abcdefghijklmno'):
    if puzzle == goal:
        return [puzzle]
    if not solvable(puzzle, goal):
        return []

    space = puzzle.find('_')
    currentMnht = mnhtPuzzle(puzzle, goal)
    openSet = [(currentMnht, 0, (puzzle, space))] # est, lvl, (puzzle, its space)
    heapq.heapify(openSet)
    closedSet = {}

    while True:
        est, lvl, pzl = heapq.heappop(openSet)
        pzStr, space = pzl # pzl = puzzle string, space location of current puzzle
        if pzStr in closedSet: # only want to put the string in closedSet
            continue
        else:
            closedSet[pzStr] = lvl

        for nbr in neighbors(pzStr, space):
            nbrPzl, nbrSpace = nbr
            newLvl = lvl + 1
            if nbrPzl == goal:
                return getPath(nbrPzl, newLvl, closedSet)
            elif nbrPzl in closedSet:
                continue
            else:
                newEst = updateEst(space, nbrSpace, pzStr[nbrSpace], est)
                heapq.heappush(openSet, (newEst, newLvl, nbr))


# solving puzzles in the file one-by-one
countTotalTime = time.clock()
for pzl in FILE:
    start = time.clock()
    if '0' in pzl:
        pzl = pzl[0:pzl.find('0')].lower() + '_' + pzl[pzl.find('0') + 1:].lower()
    printList = [n.find('_') for n in solve(pzl.strip(), GOAL)]
    # printList is the sequence of indexes that the space moves to in each move
    elapsed = round(time.clock() - start, 3)
    lvl = len(printList) - 1
    if len(printList) == 0:
        print('Puzzle: {} is unsolvable.'.format(pzl.strip()))
    else:
        print('{} : {} TIME: {}s SEQUENCE: {}'.format(pzl.strip(), lvl, elapsed, printList))
print('Time: ', round(time.clock() - countTotalTime, 4))
