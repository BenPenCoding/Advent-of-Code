file = open("puzzle.txt","r")

puzzleArray = []

for line in file:

    puzzleArray.append(line)

print(puzzleArray)

pointer = 49

array = []

for i in range(100):

    array.append(i)

def shiftPointer(pointer, rotation):

    if rotation[0] == 'L':

        pointer -= rotation[0]

        if pointer < 0:

            pointer += 100

    else:

        pointer += rotation[1]

        if pointer > 99:

            pointer -= 100

    return pointer


