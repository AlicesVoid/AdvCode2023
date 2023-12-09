# Open the File and Return the Content
def openFile(path):
    # Open File
    with open(path) as f:
        content = f.readlines()
        return content

# Strip the Content into Lists
def parseContent(content):
    # Parse Content
    for i in range(len(content)):
        content[i] = content[i].strip()
    return content

class oasisPuzzle:
    def __init__(self, rows):
        self.rows = rows
        self.zeroRows = self.findZeroDiffs()
        self.nextVals = self.findNextVals()
        self.prevVals = self.findPrevVals()
        self.total = sum(self.nextVals)
        self.prevTotal = sum(self.prevVals)

    # Mostly Debugging
    def printTotal(self):
        print(self.total)
    def printPrevTotal(self):
        print(self.prevTotal)
    def printPrevVals(self):
        print(self.prevVals)
    def printNextVals(self):
        print(self.nextVals)
    def printRows(self):
        for i in range(len(self.rows)):
            print(self.rows[i])
    def printZeroDiffEnds(self):
        for i in range(len(self.zeroRows)):
            print(self.zeroRows[i][-1])
    
    # Finds the Zero Diff for Each Row in Rows 
    def findZeroDiffs(self):
        zeroDiffs = []
        for row in self.rows:
            zeroDiffs.append(findZeroDiffs(row))
        return zeroDiffs

    # Finds the NextVal for each Zero Diff 
    def findNextVals(self):
        nextVals = []
        for row in self.zeroRows:
            nextVals.append(findNextVal(row))
        return nextVals
    
    # Finds the PrevVal for each Zero Diff 
    def findPrevVals(self):
        prevVals = []
        for row in self.zeroRows:
            prevVals.append(findPrevVal(row))
            # print(prevVals)
        return prevVals

# Finds the Difference for each row
def findRowDiffs(row):
    diffs = []
    for i in range(0, len(row) - 1):
        diffs.append(row[i+1] - row[i])
    return diffs

# Finds the Diffs until they all equal zero. Stores them
def findZeroDiffs(row):
    zeroDiffs = [row]
    rowDiffs = row
    check = True
    
    while sum(zeroDiffs[-1]) != 0 or check:
        
        rowDiffs = findRowDiffs(rowDiffs)      
        zeroDiffs.append(rowDiffs)
        
        for i in rowDiffs:
            if i == 0:
                check = False
            else:
                check = True
                
        # print(rowDiffs, zeroDiffs)  
        # print(rowDiffs, zeroDiffs[-1], sum(zeroDiffs[-1]) == 0)

    return zeroDiffs

# Finds the New Value 
def findNextVal(rowDiffs):
    nextVal = 0
    for i in range(len(rowDiffs)):
        nextVal += rowDiffs[i][-1]
    return nextVal

# Finds the Previous Value 
def findPrevVal(rowDiffs):
    prevVal = 0        
        
    for i in range(0, len(rowDiffs)-1):
        print(rowDiffs[i][0])
        if i % 2 == 0: 
            prevVal += rowDiffs[i][0]
        else:
            prevVal -= rowDiffs[i][0]

    # print('PrevVal:', prevVal)   
    return prevVal

# Creates the Oasis Puzzle
def createOasisPuzzle(input):
    rows = []
    for i in range(len(input)):
        puzzleLine = []
        line = input[i].split(' ')
        for val in line:
            puzzleLine.append(int(val))
        rows.append(puzzleLine)
    return oasisPuzzle(rows)

# Part 1 Code
def part1(path):

    # Open File
    content = openFile(path)
    input = parseContent(content)
    puzzle = createOasisPuzzle(input)
    # puzzle.printNextVals()
    puzzle.printZeroDiffEnds()
    puzzle.printTotal()
    

# Part 2 Code
def part2(path):
    
        # Open File
    content = openFile(path)
    input = parseContent(content)
    puzzle = createOasisPuzzle(input)
    # puzzle.printNextVals()
    # puzzle.printPrevVals()
    puzzle.printPrevTotal()
    
# Part 1 
# part1('input.txt')

# Part 2
part2('test1.txt')