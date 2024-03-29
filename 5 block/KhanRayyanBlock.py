'''
block problem due 11-14-18
given a certain area, figure out how to arrange
the given rectangular blocks so that they fit
exactly. should be run from the command line, and
the first two numbers of the arguments following
the script are the height and width of the given
area -- e.g. "> python KhanRayyanBlock.py 4x5"
would denote an area of height 4 and width 5.
They may be separated by either an 'x' or a space.
The numbers following those describing the area
are meant to denote the areas of the rectangular
pieces meant to fit inside the area, also separated
by either an 'x' or a space. Therefore, something
like ">python KhanRayyanBlock.py 15x5 3 4 4 7 15x1 1 5 5x3"
would be interpreted as you wanting to fit rectangles of
sizes 3x4, 4x7, 15x1, 1x5, and 5x3 into an area of 15x5.

In the process of trying to fit the rectangles into the
area, they might be rotated, which the output will
reflect -- the height for a certain rotation will always
be printed before its width. So if a rectangle is input
as "3x4" but only fits into the area if it's vertically
4 units, the output will show it as "4x3". The output
lists the rectangles in the order of right to left, top
to bottom. The first rectangle in the outputted sequence
will be the uppermost, leftmost rectangle as it fits into
the area, and the following one will be the highest one to
its right, and so on. The counting always counts the
highest one to the right until it hits the right edge of
the area and wraps around, basically.
'''

import sys
import time
from tkinter import *

# input
INPUTLIST = sys.argv

INPUT = ' '.join(INPUTLIST[1:]).replace('x', ' ').split(' ')
# input should be all numbers individually regardless of if separated by x or space

# take input and create board and blocks
BOARDW, BOARDH = int(INPUT[1]), int(INPUT[0]) # board width and height
START = {y: ''.join(['.' for n in range(BOARDW)]) for y in range(BOARDH)}
        # dict w/ y as key and string as value
BLOCKS = {int(index/2): (INPUT[index], INPUT[index + 1]) for index in range(2, len(INPUT), 2)}
        # set of blocks represented by (width, height)
replace = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
CHOICES = {key: replace[key] for key in BLOCKS}


# helper methods:

# one time calls:
def areaAddsUp(boardw, boardh, blx): # to check if impossible before trying to solve
    totalArea = boardw*boardh
    blockArea = sum([int(blx[key][0])*int(blx[key][1]) for key in blx])
    if totalArea != blockArea:
        return False
    return True


def printBoard(board):
    for key in board: # print each row
        print(' '.join(board[key])) # characters separated by a space
    if BOARDW > 30 or BOARDH > 30:
        print('\n') # if its a big puzzle leave more space around it
    else:
        print('')


def output(board):
    if board == False:
        return 'No solution.'

    seen = set()
    output = []
    reverseChoices = {CHOICES[key]:key for key in CHOICES}
    # reverse to take string value representing piece id and get the int id
    # made some of them letters because it looked nicer printing than 2-digit numbers
    # not actually necessary but don't think it makes a huge difference?

    for key in board: # for each row
        for index in range(len(board[key])): # check label of index
            row = board[key]
            label = row[index]
            if label in seen: # if you've already seen it whatever
                continue
            seen.add(label) # otherwise add to seen
            height, width = BLOCKS[int(reverseChoices[label])] # get the h/w if its block

            if index + int(width) - 1 == row.rfind(label):
                # if the last occurrence of the label is at the index + width
                output.append('{}x{}'.format(height, width)) # add h, w to output
            else:
                # otherwise put it in as w, h
                output.append('{}x{}'.format(width, height))
    return output


def solve(board, currentRow, choices):
    if areaAddsUp(BOARDH, BOARDW, BLOCKS):
        return output(solve1(board, currentRow, choices))
    else:
        return 'Blocks do not fit area.'


# repeatedly called
def canAdd(width, height, topLeftCorner, board):
    x, y = topLeftCorner
    if (x + width) > BOARDW: # if adding block goes off the board width
        return False
    elif (y + height) > BOARDH: # if adding block goes off the board height
        return False
    elif board[y][x:x + width].count('.') < width: # if there is overlap
        return False
    return True


def addBlock(height, width, blockNum, topLeftCorner, board): # height, width, block id, location, board
    x, y = topLeftCorner # column/row
    marker = CHOICES[blockNum] # id to denote puzzle

    # check if possible to add block:
    if canAdd(width, height, topLeftCorner, board): # if it is possible to add, add it
        boardCopy = board.copy() # copy necessary because it's a dict
        for dep in range(y, y + height): # modify each row
            boardCopy[dep] = board[dep][0:x] + marker*width + board[dep][x + width:]
        return boardCopy

    return False # if the block doesn't fit in this space


# method to search for puzzle solution:
def solve1(board, currentRow, choices):
    if '.' not in board[BOARDH - 1]: # if the bottom row is filled then its solved
        return board

    if '.' in board[currentRow]: # if there's an empty space in current row its topleft
        nextOpenIndex = board[currentRow].find('.')
    else:
        while '.' not in board[currentRow]: # otherwise find row with empty space
            currentRow += 1
        nextOpenIndex = board[currentRow].find('.')

    for choice in choices:
        newChoices = choices.copy()
        newChoices.pop(choice) # copy of choices without choice
        height, width = int(BLOCKS[choice][0]), int(BLOCKS[choice][1])

        for rotation in range(2):
            if rotation == 0:
                newBoard = addBlock(height, width, choice,
                                    (nextOpenIndex, currentRow), board) # create board with added block
                if newBoard: # if it's actually made it's valid so pass it on
                    result = solve1(newBoard, currentRow, newChoices)
                    if result:
                        return result

            if height != width and rotation == 1: # if its not a square try rotating
                width, height = int(BLOCKS[choice][0]), int(BLOCKS[choice][1])
                newBoard = addBlock(height, width, choice,
                                    (nextOpenIndex, currentRow), board)
                if newBoard:
                    result = solve1(newBoard, currentRow, newChoices)
                    if result:
                        return result
    return False # no solution


# output
start = time.clock()
print(solve(START, 0, CHOICES))
print('Total time: {} seconds.'.format(round(time.clock() - start, 3)))
