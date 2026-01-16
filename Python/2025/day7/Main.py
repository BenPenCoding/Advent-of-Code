'''

class Beam():

    def __init__(self, row, column):

        self.row = row
        self.column = column
        self.symbol = '|'

        diagram[self.row][self.column] = '|'

    def getCoords(self):

        return [self.row, self.column]

    def populateDown(self):

        while True:

            if self.row + 1 >= len(diagram):

                break

            else:

                if diagram[self.row + 1][self.column] == "^":

                    break
                
                else:
                
                    diagram[self.row + 1][self.column] = "|"
                    self.row += 1

#Part 1

global diagram
diagram = []

file = open("/Users/benpennycook/Library/CloudStorage/OneDrive-DurhamUniversity/Desktop/Git Repos/Advent-of-Code/Python/2025/day7/puzzle.txt", "r")

for line in file:

    diagram.append(list(line.replace("\n", "")))

file.close()

beamEntrance = [1, diagram[0].index("S")]

beamList = []

beamList.append(Beam(beamEntrance[0], beamEntrance[1]))

splits = 0

for row in range(len(diagram)):

    for beam in beamList:

        beam.populateDown()

    if "^" in diagram[row]:

        for character in range(len(diagram[row])):

            if diagram[row][character] == "^":

                for beam in beamList:

                    if beam.getCoords() == [row - 1, character]:

                        beamList.remove(beam)
                        splits += 1

                if diagram[row][character - 1] != "|":

                    beamList.append(Beam(row, character - 1))

                if diagram[row][character + 1] != "|":

                    beamList.append(Beam(row, character + 1))

print(splits)

'''

#Part 2 attempt 1

'''

class Beam():

    def __init__(self, row, column, diagram):

        self.row = row
        self.column = column
        self.symbol = '|'
        self.diagram = diagram

        self.diagram.changeData(self.row, self.column, '|')

    def getCoords(self):

        return [self.row, self.column]

    def populateDown(self):

        while True:

            if self.row + 1 >= len(self.diagram.getData()):

                break

            else:

                if self.diagram.getData()[self.row + 1][self.column] == "^":

                    break
                
                else:
                
                    self.diagram.changeData(self.row + 1, self.column, "|")
                    self.row += 1

class Diagram():

    def __init__(self, data):

        self.data = data
        self.beamList = []

    def addBeam(self, beam):

        self.beamList.append(beam)

    def showData(self):

        for row in self.data:

            print(row)

    def getData(self):

        return self.data

    def changeData(self, row, column, newData):

        self.data[row][column] = newData

    def populateDownAll(self):

        for beam in self.beamList:

            beam.populateDown()

    def removeBeam(self, beam):

        self.beamList.remove(beam)

global diagrams
diagrams = []

startDiagramData = []

file = open("/Users/benpennycook/Library/CloudStorage/OneDrive-DurhamUniversity/Desktop/Git Repos/Advent-of-Code/Python/2025/day7/puzzle.txt", "r")

for line in file:

    startDiagramData.append(list(line.replace("\n", "")))

file.close()

beamEntrance = [1, startDiagramData[0].index("S")]

startDiagram = Diagram(startDiagramData)

startDiagram.addBeam(Beam(beamEntrance[0], beamEntrance[1], startDiagram))

startDiagram.populateDownAll()

diagrams.append(startDiagram)

for row in range(len(startDiagram.getData())):

    for diagram in diagrams:

        diagram.populateDownAll()

        if "^" in diagram.getData()[row]:

'''

#Part 2 attempt 2







