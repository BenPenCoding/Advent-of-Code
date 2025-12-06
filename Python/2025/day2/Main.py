#Part 1


file = open("/Users/benpennycook/Library/CloudStorage/OneDrive-DurhamUniversity/Desktop/Git Repos/Advent-of-Code/Python/2025/day2/puzzle.txt", "r")

for line in file:
    text = line

tempRangeArray = text.split(",")

rangeArray = []

for IDRange in tempRangeArray:

    tempRangeArray = IDRange.split("-")

    rangeArray.append([tempRangeArray[0],tempRangeArray[1]])

InvalidIDs = []

'''
for IDRange in rangeArray:

    start = int(IDRange[0])

    end = int(IDRange[1])

    for ID in range(start, end+1):

        ID = str(ID)

        IDLength = len(ID)

        if ID[:int(IDLength/2)] == ID[int(IDLength/2):]:

            InvalidIDs.append(int(ID))

print(f"Part 1: {sum(InvalidIDs)}")
'''

#Part 2

def isRepeating(partString, fullString):

    fullString = fullString.replace(partString, "")

    if fullString:

        return False

    return True

for IDRange in rangeArray:

    start = int(IDRange[0])

    end = int(IDRange[1])

    for ID in range(start, end+1):

        ID = str(ID)

        string = ""

        for character in ID[:int(len(ID)/2)]:

            string += character

            if isRepeating(string, ID):

                InvalidIDs.append(int(ID))
                break

        
print(f"Part 2: {sum(InvalidIDs)}")

