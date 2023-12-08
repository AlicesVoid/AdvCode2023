import math

# Open the File and Return the Content
def openFile(path):
    # Open File
    with open(path) as f:
        content = f.readlines()
        return content
    
# Create a Class for the Map Path
class mapPath:
    # Constructor
    def __init__(self, method, map):
        self.method = method
        self.map = parseMap(map)
        self.start = 'A'
        self.end = 'Z'
        self.count = 0
    
    # Print the Count 
    def printCount(self):
        print(self.count)
    
    # DebuggingTool
    def debugTool(self):
        print(self.method)
        print(self.map)
        print(self.count)
    
    def solveMap(self):
        # Set the Current Location
        currLoc = self.start
        methLen = len(self.method)
        
        # Iterate Through the Map
        while currLoc != self.end:
            
            move = self.method[self.count % methLen]
            
            # Get the Next Location           
            nextLoc = self.map[currLoc][move]
            
            # Update the Count
            self.count += 1
            
            # Update the Current Location
            currLoc = nextLoc
            
        # Print the Count
        self.printCount()
        
    def solveAllMap(self):
        # Set the Current Location Array
        currLoc = []
        methLen = len(self.method)
        allEnds = []
        foundEnds = []
        
        # Each Key in map that ends with self.start is added to currLoc 
        for key in self.map:
            if key.endswith(self.start):
                currLoc.append(key)
            elif key.endswith(self.end):
                allEnds.append(key)
        
        # print(len(currLoc), currLoc)
        # print(len(allEnds), allEnds)
        # print(len(foundEnds), foundEnds)
        # print(len(allEnds) == len(foundEnds))
        
        while len(allEnds) != len(foundEnds):
            
            index = self.count % methLen
            toRm = []
            toAd = []
            
            # For Each Current Location
            for loc in currLoc:
                                
                # Iterate Through the Map
                move = self.method[index]
                                
                # Get the Next Location           
                nextLoc = self.map[loc][move]
                                
                # If nextLoc is in allEnds, remove that value from allEnds
                if nextLoc in allEnds:
                    foundEnds.append(self.count + 1)
                
                # Add nextLoc to toAd and toRm
                toAd.append(nextLoc)
                toRm.append(loc)
                
                
            # print(toAd, toRm)
            
            # if len(foundEnds) != 0:
                # print('Found:', len(foundEnds), 'of', len(allEnds), 'at:', self.count)
            
            
            for i in range(0, len(toAd)):
                # print('Adding:',toAd[i],'Removing:',toRm[i])
                currLoc.append(toAd[i])
                currLoc.remove(toRm[i])
                         
            self.count += 1
                    
        # Lowest Common Multiple between all values in foundEnds 
        lcm = 1
        for val in foundEnds:
            print('value:', val, 'lcm:', lcm, 'gcd:' , math.gcd(lcm, val))
            if lcm == 1:
                lcm = val
            else:
                lcm = lcm * val // math.gcd(lcm, val)
                    
        print(lcm)
            
        
        


# Create a Dictionary from the Map  
def parseMap(map):
    mapDict = {}
    
    # Iterate Through Map
    for item in map:
        
        # Nested Dictionary 
        dirDict = {}
        dirDict['L'] = item[1]
        dirDict['R'] = item[2]
        
        # mapDict[AAA] = {'L': 'BBB', 'R': 'CCC'}
        mapDict[item[0]] = dirDict 
    
    return mapDict
          
# Part 1 Code
def part1(path):

    map = []

    # Open File
    content = openFile(path)
    
    # Iterate Through Content
    for line in content:
        # For the first line, store it as a string
        if line == content[0]:
            input = line.split()
            method = input[0]           
            
        elif line != content[1]:
            # Split Input and Parse
            input = line.split()
            #print(input)
            
            item = []
            item.append(input[0])
            
            # Remove the First Character from input[2] and the last character from input[3]
            item.append(input[2][1:-1])
            item.append(input[3][:-1]) 
            
            # Append to Map 
            map.append(item)
            
            
    # print(method)        
    # print(map)
    fullMap = mapPath(method, map)
    fullMap.solveMap()
  
# Part 2 Code
def part2(path):
    
    map = []

    # Open File
    content = openFile(path)
    
    # Iterate Through Content
    for line in content:
        # For the first line, store it as a string
        if line == content[0]:
            input = line.split()
            method = input[0]           
            
        elif line != content[1]:
            # Split Input and Parse
            input = line.split()
            #print(input)
            
            item = []
            item.append(input[0])
            
            # Remove the First Character from input[2] and the last character from input[3]
            item.append(input[2][1:-1])
            item.append(input[3][:-1]) 
            
            # Append to Map 
            map.append(item)
            
    # print('Appending Done')      
    # print(method)        
    # print(map)
    fullMap = mapPath(method, map)
    fullMap.solveAllMap()
    
# Part 1 
# part1('input.txt')

# Part 2
part2('test2.txt')
part2('input.txt')