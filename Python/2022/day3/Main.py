file = open("Python/2022/day3/puzzle.txt", "r")

rucksacks = []

for line in file:

    string = line.replace('\n', '')
    rucksacks.append([string[:int(len(string)/2)], string[int(len(string)/2):]])

file.close()

def convertToPriority(item):

    if ord(item) >= 97:

        return ord(item) - 96
    
    else:

        return ord(item) - 38

totalPriority = 0

for rucksack in rucksacks:

    comp1 = rucksack[0]
    comp2 = rucksack[1]

    usedLetters = []

    for letter in comp1:

        if letter in comp2 and letter not in usedLetters:

            totalPriority += convertToPriority(letter)

            usedLetters.append(letter)

print(f"Part 1: {totalPriority}")

totalPriority = 0

threeRucksacks = []

for i in range(0, len(rucksacks), 3):

    tempRucksack = []

    for j in range(3):

        tempRucksack.append(rucksacks[i+j][0] + rucksacks[i+j][1])

    threeRucksacks.append(tempRucksack)

for rucksacks in threeRucksacks:

    rucksack1 = rucksacks[0]
    rucksack2 = rucksacks[1]
    rucksack3 = rucksacks[2]

    usedLetters = []

    for letter in rucksack1:

        if letter not in usedLetters and letter in rucksack2 and letter in rucksack3:

            #print(f"{letter} : {convertToPriority(letter)}")
            totalPriority += convertToPriority(letter)
            break

        else:

            usedLetters.append(letter)

print(f"Part 2: {totalPriority}")
    
