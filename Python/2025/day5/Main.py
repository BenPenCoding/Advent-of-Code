#Part 1

file = open("/Users/benpennycook/Library/CloudStorage/OneDrive-DurhamUniversity/Desktop/Git Repos/Advent-of-Code/Python/2025/day5/puzzle.txt", "r")

reachedBlank = 0

rangeArray = []

IDArray = []

for line in file:

    if line == "\n":

        reachedBlank = 1

        continue

    if reachedBlank == 0:

        rangeArray.append(line.replace("\n", ""))

    else:

        IDArray.append(int(line.replace("\n", "")))

tempArray, rangeArray = rangeArray, []

for IDRange in tempArray:

    rangeArray.append([int(IDRange[:IDRange.index("-")]), int(IDRange[IDRange.index("-") + 1:])])

numFresh = 0

for ID in IDArray:

    for IDRange in rangeArray:

        if IDRange[1] - ID >= 0 and IDRange[1] - ID <= IDRange[1] - IDRange[0]:

            numFresh += 1

            break

print(numFresh)

#Part 2

def fixOverlaps(rangeArray):

    merged = []

    for i in range(len(rangeArray)):

        if i == 0:

            merged.append(rangeArray[i])

        else:

            range1 = merged[-1]
            range2 = rangeArray[i]

            if range1 == range2:

                continue

            if range1[1] >= range2[0] and range2[1] > range1[1]:

                merged[-1] = [range1[0], range2[1]]

            else:

                merged.append(range2)

    return merged

rangeArray.sort()

rangeArray = fixOverlaps(rangeArray)

total = 0

for IDRange in rangeArray:

    total += IDRange[1] - IDRange[0] + 1

print(total)