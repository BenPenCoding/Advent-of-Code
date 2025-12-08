#Part 1

file = open("/Users/benpennycook/Library/CloudStorage/OneDrive-DurhamUniversity/Desktop/Git Repos/Advent-of-Code/Python/2025/day6/puzzle.txt", "r")

dataArray = []

for line in file:

    dataArray.append(line.replace("\n", ""))

file.close()

def removeDoubleSpaces(text):

    returnText = ""

    for character in range(0,len(text)-1):

        if text[character] == " " and text[character + 1] == " ":

            continue

        else:

            returnText += text[character]

    returnText += text[-1]

    return returnText

'''

for i in range(len(dataArray)):

    dataArray[i] = removeDoubleSpaces(dataArray[i])
    dataArray[i] = dataArray[i].split(" ")
    dataArray[i] = [x for x in dataArray[i] if x != ""] if i == 4 else [int(x) for x in dataArray[i] if x != ""]

sum = 0

for i in range(len(dataArray[0])):

    operator = dataArray[4][i]

    if operator == "+":

        sum += dataArray[0][i] + dataArray[1][i] + dataArray[2][i] + dataArray[3][i]


    else:

        sum += dataArray[0][i] * dataArray[1][i] * dataArray[2][i] * dataArray[3][i]

print(sum)
'''

#Part 2

file = open("/Users/benpennycook/Library/CloudStorage/OneDrive-DurhamUniversity/Desktop/Git Repos/Advent-of-Code/Python/2025/day6/puzzle.txt", "r")

dataArray = []

for line in file:

    dataArray.append(line.replace("\n", ""))

file.close()

#Get operators

dataArray[-1] = dataArray[-1].replace(" ", "")

operators = []

for operator in dataArray[-1]:

    operators.append(operator)

#Parse other nums

numArray = [[]]

numArrayIndex = 0

for i in range(len(dataArray[0]) - 1, -1, -1):

    checkStr = ""

    for j in range(len(dataArray)- 1):

        checkStr += dataArray[j][i]

    if not checkStr.replace(" ", ""):

        #THE LINE IS A GAP
        numArrayIndex += 1
        numArray.append([])
        continue

    numStr = ""

    for j in range(len(dataArray)- 1):

        numStr += dataArray[j][i]

    numArray[numArrayIndex].append(int(numStr))

numArray = numArray[::-1]

sum = 0

for i in range(len(numArray)):

    if operators[i] == "*":

        tempSum = 1

        for num in numArray[i]:       
        
            tempSum *= num

    else:

        tempSum = 0

        for num in numArray[i]:       
        
            tempSum += num

    sum += tempSum

print(sum)




