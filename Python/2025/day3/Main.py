#Part 1

file = open("/Users/benpennycook/Library/CloudStorage/OneDrive-DurhamUniversity/Desktop/Git Repos/Advent-of-Code/Python/2025/day3/puzzle.txt", "r")

batteryArray = []

for line in file:

    batteryArray.append(line.replace("\n", ""))

joltageArray = []

'''

for batteryLine in batteryArray:

    joltageArray.append(int(f"{max(batteryLine[:-1])}{max(batteryLine[batteryLine.index(max(batteryLine[:-1])) + 1:])}"))

print(sum(joltageArray))
'''

#Part 2

def findBestBatteries(batteries, numBatteriesLeft):

    if numBatteriesLeft == 1:

        return f"{max(batteries)}"

    else:

        return max(batteries[0:len(batteries) - numBatteriesLeft + 1]) + findBestBatteries(batteries[batteries.index(max(batteries[0:len(batteries) - numBatteriesLeft + 1])) + 1:], numBatteriesLeft - 1)

for batteryLine in batteryArray:

    joltageArray.append(int(findBestBatteries(batteryLine, 12)))

print(sum(joltageArray))