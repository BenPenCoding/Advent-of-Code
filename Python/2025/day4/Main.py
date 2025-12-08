#Part 1

file = open("/Users/benpennycook/Library/CloudStorage/OneDrive-DurhamUniversity/Desktop/Git Repos/Advent-of-Code/Python/2025/day4/puzzle.txt", "r")


paperArray = []

for line in file:

    paperArray.append(line.replace("\n", ""))


def checkAccess(row, column, paperArray):

    numReels = 0
    
    for i in range(-1, 2, 1):

        for j in range(-1, 2, 1):

            if i == 0 and j == 0:

                continue

            else:

                if row + i > -1 and row + i < len(paperArray):

                    if column + j > -1 and column + j < len(paperArray[0]):

                        if paperArray[row + i][column + j] == "@":

                            numReels += 1

    return True if numReels < 4 else False

numAccessible = 0

for row in range(len(paperArray)):

    for column in range(len(paperArray[0])):

        if paperArray[row][column] == "@":

            if checkAccess(row, column, paperArray):

                numAccessible += 1

print(numAccessible)


            
#Part 2

def checkAccess(row, column, paperArray):

    numReels = 0
    
    for i in range(-1, 2, 1):

        for j in range(-1, 2, 1):

            if i == 0 and j == 0:

                continue

            else:

                if row + i > -1 and row + i < len(paperArray):

                    if column + j > -1 and column + j < len(paperArray[0]):

                        if paperArray[row + i][column + j] == "@":

                            numReels += 1

    return True if numReels < 4 else False

def checkAll(paperArray):

    removeArray = []

    for row in range(len(paperArray)):

        for column in range(len(paperArray[0])):

            if paperArray[row][column] == "@":

                if checkAccess(row, column, paperArray):

                    removeArray.append([row, column])

    return removeArray

def removeAll(paperArray, removeCount, removeArray):

    for coordinates in removeArray:

        string = paperArray[coordinates[0]] 

        stringArray = list(string)

        stringArray[coordinates[1]] = "."

        string = "".join(stringArray)

        paperArray[coordinates[0]] = string

        removeCount += 1

    return paperArray, removeCount

removeCount = 0

while True:

    removeArray = checkAll(paperArray)

    if removeArray:

        paperArray, removeCount = removeAll(paperArray, removeCount, removeArray)

    else:

        break

print(removeCount)