'''
word ladder lab, to turn in friday, september 14.

word ladder was a short assignment concurrent with the 
slider puzzle unit. the assignment sheet is in this folder.
we spent about two days on it in class and after implementing
the suggestion about letter swapping (rather than directly 
comparing the 5000 words in the file to each other), this 
should run significantly (about 5000/26 times) better 
than average. 
'''

import time
import math
import sys


start = time.clock()
file = open("words.txt", "r")
numNeighbors = 0
wordList = []

for line in file:
    wordList.append(line.strip())


def isNeighbor(word1, word2):
    matches = 0
    for n in range(0, len(word1)):
        if word1[n] == word2[n]:
            matches = matches+1
    if matches == len(word1)-1:
        return True
    else:
        return False


def genKeys(word):
    keys = []
    for n in range(0, len(word)):
        key = word[0:n] + "_" + word[n+1:]
        keys.append(key)
    return keys


def toGraph(list):
    dict = {}
    dictSpaces = {}
    for word in list:
        keys = genKeys(word)
        for k in keys:
            if k in dictSpaces:
                dictSpaces[k].append(word)
            else:
                dictSpaces[k] = [word]
    for key in dictSpaces:
        for w in dictSpaces[key]:
            if w in dict:
                dict[w].extend([*dictSpaces[key]])
                dict[w].remove(w)
            else:
                dict[w] = [*dictSpaces[key]]
                dict[w].remove(w)
    return dict


def numPairs(dict):
    total = 0
    for k in dict:
        total = total + len(dict[k])
    return total/2


def mostNeighbors(dict):
    mostNbrs = 0
    nbr = ''
    for k in dict:
        curr = len(dict[k])
        if curr > mostNbrs:
            nbr = k
            mostNbrs = curr
    return nbr


def hasNumNbrs(num, dict):
    ct = 0
    for k in dict:
        if len(dict[k])==num:
            ct = ct+1
    return ct


def numLonePairs(dict):
    ct = 0
    for k in dict:
        if len(dict[k]) == 1:
            if len(dict[dict[k][0]]) == 1:
                ct = ct + 1
    return ct/2


def findDegrees(dict):
    degLst = []
    for k in dict:
        if len(dict[k]) not in degLst:
            degLst.append(len(dict[k]))
    return degLst


def distictComponents(dict):
    sizes = set()
    for k in dict:
        seen = {k}
        parseMe = [k]
        while parseMe:
            word = parseMe.pop(0)
            for n in dict[word]:
                if n not in seen:
                    parseMe.append(n)
                    seen.add(n)
        compSize = len(seen)
        if compSize not in sizes:
            sizes.add(compSize)
    return sizes


def k3(dict):
    k3 = 0
    for k in dict:
        seen = {k}
        parseMe = [k]
        while parseMe:
            word = parseMe.pop(0)
            for n in dict[word]:
                if n not in seen:
                    parseMe.append(n)
                    seen.add(n)
            compSize = len(seen)
            if compSize == 3:
                k3 = k3+1
    return k3/3


def widestPair(dict):
    startWord = ''
    endWord = ''
    for k in dict:
        seen = {k}
        parseMe = [k]
        while parseMe:
            word = parseMe.pop(0)
            for n in dict[word]:
                if n not in seen:
                    parseMe.append(n)
                    seen.add(n)
            compSize = len(seen)
            if compSize == 1625:
                startWord = k
                endWord = word

    return "Start: ", startWord, " End: ", endWord


gr = toGraph(wordList)
for k in gr:
    print(k, ": ", gr[k])

# part 1: count words
lines = open('words.txt', 'r')
count = 0
for line in lines:
    count = count+1
print("Number of words: ", count)

# Part 2: Count pairs
print("Neighbor pairs: ", int(numPairs(gr)))

# Part 3: Print time
print("Time to do #2: ", round(time.clock() - start, 4), " seconds")

# Part 4: List neighbors of given word
# if len(sys.argv) == 2:
#    print("Word: ", sys.argv[1], " Neighbors: ", gr[sys.argv[1]] )

# Part 5: print the word with the greatest number of neighbors
print("Word with the most neighbors: ", mostNeighbors(gr))

# Part 6: print out the number of words with no neighbors
print("There are ", hasNumNbrs(0, gr), " words with 0 neighbors.")

# part 7: print out the pairs of words that only have each other as neighbors
print("2-cliques: ", numLonePairs(gr))

# part 8: print out the number of distinct degrees, and a list of the distinct degrees
lst = findDegrees(gr)
print("Number of distinct degrees: ", len(lst))

# part 9: print number of distict component sizes
print("Component sizes: ", len(distictComponents(gr)))

# part 10: print number of 3-cliques
print("K3s: ", k3(gr))

# bonus
print(widestPair(gr))
