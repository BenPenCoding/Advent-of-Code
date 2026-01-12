file = open("Python/2022/day1/puzzle.txt", "r")

string = ''

for line in file:

    string += line


calorieList = []
calorieSum = 0

for calorie in string.split("\n"):

    if calorie == '':

        calorieList.append(calorieSum)
        calorieSum = 0

    else:

        calorieSum += int(calorie)

calorieList.append(calorieSum)

print(f"Part 1: {max(calorieList)}")

calorieList.sort(reverse = True)

print(f"Part 2: {calorieList[0] + calorieList[1] + calorieList[2]}")
        

