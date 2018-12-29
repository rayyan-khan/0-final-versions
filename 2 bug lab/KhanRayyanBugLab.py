'''
bug lab due 9-24-18
find the solution to the problem given at
https://artofproblemsolving.com/wiki/index.php?title=2018_AIME_I_Problems#Problem_10
but with for any given number of spokes or steps.
'''


import time
import sys
start=time.clock()


class position():
    pos = ''
    level = 0

    def __init__(self, position, level):
        self.level = level
        self.pos = position

    def getPos(self):
        return self.pos

    def getLevel(self):
        return self.level


def neighbors(pos, maxSpoke):
    nbrs = []
    if pos.isupper():
        nbrs.append(pos.lower())
        if ord(pos) == maxSpoke:
            nbrs.append('A')
        else:
            nbrs.append(chr(ord(pos) + 1))
    else:
        nbrs.append(pos.upper())
        if pos == 'a':
            nbrs.append(chr(32+maxSpoke))
        else:
            nbrs.append(chr(ord(pos)-1))
    return nbrs


def bfs(numSpokes, numSteps):
    numSteps = numSteps+1
    maxSpoke = 64 + numSpokes
    upperWays = {chr(n):[0 for n in range(numSteps)] for n in (range(65, 65+numSpokes))}
    lowerWays = {chr(n):[0 for n in range(numSteps)] for n in (range(97, 97+numSpokes))}
    dictWays = {**upperWays, **lowerWays}  #dictWays[letter position] = [ways to reach per level, index = level]
    parseMe = [position('A', 0)]
    sum = 0

    while sum<2**numSteps:
        sum += 1
        current = parseMe.pop(0)
        currPos = current.getPos()
        lvl = current.getLevel()
        if lvl<numSteps:
            dictWays[currPos][lvl] += 1
        nbrLvl = lvl+1
        for k in neighbors(currPos, maxSpoke):
            parseMe.append(position(k,nbrLvl))
    return dictWays


def printDict(d):
    for k in d:
        print(k,': ', end='')
        print(*d[k], sep=', ')


numSpokes = 5 if len(sys.argv)<2 else int(sys.argv[1])
steps = 12 if len(sys.argv)<3 else int(sys.argv[2])
print("Ways to reach ", numSpokes*2 , " spots in a double spoked wheel in ", steps, " steps.")
printDict(bfs(numSpokes,steps))
print('time=',time.clock()-start)