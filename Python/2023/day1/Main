total = 0
var = 0

words = ["one","two","three","four","five","six","seven","eight","nine"]
nums = [1,2,3,4,5,6,7,8,9]

fileRead = open("day1input.txt","r")
dList = fileRead.readlines()
count = 0
for j in dList:
    dList[count] =dList[count].replace("one", "1")
    dList[count] =dList[count].replace("two", "2")
    dList[count] =dList[count].replace("three","3")
    dList[count] =dList[count].replace("four", "4")
    dList[count] =dList[count].replace("five", "5")
    dList[count] =dList[count].replace("six", "6")
    dList[count] =dList[count].replace("seven", "7")
    dList[count] =dList[count].replace("eight", "8")
    dList[count] =dList[count].replace("nine", "9")
    count +=1
fileRead.close()

fileWrite = open("day2input.txt","w")

for b in dList:
   fileWrite.write(b)
fileWrite.close()


file = open('day2input.txt','r')
cList = file.readlines()
for i in cList:
    nList = []
    var = 0
    for char in i:
        if char.isnumeric():
            nList.append(int(char))
        else:
            pass
    var = int(str(nList[0]) + str(nList[-1]))
    total = total + var
    
print(total)



