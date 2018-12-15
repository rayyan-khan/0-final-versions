from tkinter import *
import time

startPzl = '......ABCDEFG...........' # each for an empty triangle
setOfChoices = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}  # possible labels
def copies(tpl): # checks for copies within subhexagons
    seen = set()
    for label in tpl:
        if label != '.':
            if label in seen:
                return True  # true if it finds a copied label
            else:
                seen.add(label)
    return False  # otherwise it's still valid

def isInvalid(hexPzl):  # returns true if pzl is invalid, rewrite later maybe but idk
    hexTL = (hexPzl[0], hexPzl[1], hexPzl[2], hexPzl[6], hexPzl[7], hexPzl[8])
    hexTR = (hexPzl[2], hexPzl[3], hexPzl[4], hexPzl[8], hexPzl[9], hexPzl[10])
    hexML = (hexPzl[5], hexPzl[6], hexPzl[7], hexPzl[12], hexPzl[13], hexPzl[14])
    hexMC = (hexPzl[7], hexPzl[8], hexPzl[9], hexPzl[14], hexPzl[15], hexPzl[16])
    hexMR = (hexPzl[9], hexPzl[10], hexPzl[11], hexPzl[16], hexPzl[17], hexPzl[18])
    hexBL = (hexPzl[13], hexPzl[14], hexPzl[15], hexPzl[19], hexPzl[20], hexPzl[21])
    hexBR = (hexPzl[15], hexPzl[16], hexPzl[17], hexPzl[21], hexPzl[22], hexPzl[23])

    # adding in rows and diagonals for Q2:
    H1 = (hexPzl[0], hexPzl[1], hexPzl[2], hexPzl[3], hexPzl[4])
    H2 = (hexPzl[5], hexPzl[6], hexPzl[7], hexPzl[8], hexPzl[9], hexPzl[10], hexPzl[11])
    H3 = (hexPzl[12], hexPzl[13], hexPzl[14], hexPzl[15], hexPzl[16], hexPzl[17], hexPzl[18])
    H4 = (hexPzl[19], hexPzl[20], hexPzl[21], hexPzl[22], hexPzl[23])
    P1 = (hexPzl[12], hexPzl[5], hexPzl[6], hexPzl[0], hexPzl[1]) # P1 = positive diagonal
    P2 = (hexPzl[13], hexPzl[14], hexPzl[7], hexPzl[8], hexPzl[2], hexPzl[3])
    P3 = (hexPzl[20], hexPzl[21], hexPzl[15], hexPzl[16], hexPzl[9], hexPzl[10], hexPzl[4])
    P4 = (hexPzl[22], hexPzl[23], hexPzl[17], hexPzl[18], hexPzl[11])
    N1 = (hexPzl[5], hexPzl[12], hexPzl[13], hexPzl[19], hexPzl[20]) # N1 = negative diagonal
    N2 = (hexPzl[0], hexPzl[6], hexPzl[7], hexPzl[14], hexPzl[15], hexPzl[21], hexPzl[22])
    N3 = (hexPzl[1], hexPzl[2], hexPzl[8], hexPzl[9], hexPzl[16], hexPzl[17], hexPzl[23])
    N4 = (hexPzl[3], hexPzl[10], hexPzl[11], hexPzl[18])

    checkCopies = {hexTL, hexTR, hexML, hexMC, hexMR, hexBL, hexBR,
                   H1, H2, H3, H4, P1, P2, P3, P4, N1, N2, N3, N4}
    # checkCopies = all the different constraints to check

    for tpl in checkCopies:
        if copies(tpl):
            return True  # true if the overall puzzle contains a subhex with copies, i.e. it's invalid

def bruteForce(pzl):  # find a solution through bruteForcing recursively
    if isInvalid(pzl):  # throw it out if it's invalid
        #print(pzl)
        return ''
    if '.' not in pzl:  # if there are no empty spaces and it's not thrown out, it's solved
        return pzl

    nextOpenIndex = pzl.find('.')
    for choice in setOfChoices:
        # make a new pzl with the next empty choice filled with a possible label
        subPzl = pzl[0:nextOpenIndex] + choice + pzl[nextOpenIndex + 1:]
        result = bruteForce(subPzl)
        if result != '': # if it didn't fail, return it!
            return result

    return ''  # failure

start = time.clock()
solution = bruteForce(startPzl)
totalTime = round(time.clock()-start, 3)
print('No solution :( Time:', totalTime) if solution == '' else print(solution, 'Time: ', totalTime)

# displaying makes it easy to check visually
window = Tk()
window.title('Hexagon Problem 2')
hexPhoto = PhotoImage(file='hexagon.gif')
pW, pH = hexPhoto.width(), hexPhoto.height()
window.geometry('{}x{}'.format(pW, pH))
canvas = Canvas(window, width=pW, height=pH)
canvas.pack()
canvas.create_image(pW/2, pH/2, image=hexPhoto)

slnR1, slnR2 = solution[0:5], solution[5:12],
slnR3, slnR4 = solution[12:19], solution[19:24]

for index, label in enumerate(slnR1):
    canvas.create_text(105+57*index, 60, text=label)
for index, label in enumerate(slnR2):
    canvas.create_text(50+57*index, 155, text=label)
for index, label in enumerate(slnR3):
    canvas.create_text(50+57*index, 245, text=label)
for index, label in enumerate(slnR4):
    canvas.create_text(105+57*index, 340, text=label)

if solution != '':
    window.mainloop()
