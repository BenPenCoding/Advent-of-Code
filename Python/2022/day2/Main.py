scoreDict = {"X": 1, "Y": 2, "Z": 3}
moveDict1 = {"X": "C", "Y": "A", "Z": "B"}
moveDict2 = {"X": "A", "Y": "B", "Z": "C"}

file = open("Python/2022/day2/puzzle.txt", "r")

totalScore = 0

for line in file:

    theirMove = line[0]
    myMove = line[2]

    score = scoreDict[myMove]

    if moveDict1[myMove] == theirMove:

        score += 6

    elif moveDict2[myMove] == theirMove:

        score += 3

    else:

        pass

    totalScore += score

print(f"Part 1: {totalScore}")


    