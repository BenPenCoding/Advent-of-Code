#Functions

def shiftPointer(pointer, rotation, numZeros):

    if rotation[0] == 'L':

        pointer -= int(rotation[1:]) % 100 


        if pointer < 0:

            pointer += 100

    else:

        pointer += int(rotation[1:]) % 100 

        if pointer > 99:

            pointer -= 100

    return pointer

#Setup

file = open("/Users/benpennycook/Desktop/Uni/Advent-of-Code/Python/2025/day1/puzzle.txt","r")

puzzleArray = []

for line in file:

    puzzleArray.append(line.replace('\n', ''))

pointer = 50

numZeros = 0

#Main

for rotation in puzzleArray:

    print(rotation)

    pointer = shiftPointer(pointer, rotation, numZeros)

    print(pointer)

    if pointer == 0:

        numZeros += 1

print(numZeros)




