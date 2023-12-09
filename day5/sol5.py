def openFile(path):
    # Open File
    with open(path) as f:
        content = f.readlines()
        return content

class seedMap:
    def __init__(self, seeds, s2s, s2f, ftw, wtl, ltt, tth, htl):
        self.seeds = seeds
        self.s2s = s2s
        self.s2f = s2f
        self.ftw = ftw
        self.wtl = wtl
        self.ltt = ltt
        self.tth = tth
        self.htl = htl

    def getLoc(self, seed):
        # print( 'Seed: ', seed, 's2s: ', self.s2s[seed], 's2f: ', self.s2f[self.s2s[seed]], 'ftw: ', self.ftw[self.s2f[self.s2s[seed]]], 'wtl: ', self.wtl[self.ftw[self.s2f[self.s2s[seed]]]], 'ltt: ', self.ltt[self.wtl[self.ftw[self.s2f[self.s2s[seed]]]]], 'tth: ', self.tth[self.ltt[self.wtl[self.ftw[self.s2f[self.s2s[seed]]]]]], 'htl: ', self.htl[self.tth[self.ltt[self.wtl[self.ftw[self.s2f[self.s2s[seed]]]]]]])

        s2s = mapValue(self.s2s, seed)
        s2f = mapValue(self.s2f, s2s)
        ftw = mapValue(self.ftw, s2f)
        wtl = mapValue(self.wtl, ftw)
        ltt = mapValue(self.ltt, wtl)
        tth = mapValue(self.tth, ltt)
        htl = mapValue(self.htl, tth)
        return htl
        # return 0
    
    def getRangeLoc(self, seedPair):
        # Does the same thing as getLoc but returns a range of values
        s2s = mapRangeValue(self.s2s, seedPair)
        s2f = mapRangeValue(self.s2f, s2s)
        ftw = mapRangeValue(self.ftw, s2f)
        wtl = mapRangeValue(self.wtl, ftw)
        ltt = mapRangeValue(self.ltt, wtl)
        tth = mapRangeValue(self.tth, ltt)
        htl = mapRangeValue(self.htl, tth)
        return htl
    
    def getSmallestLoc(self):
        smallest = 100000000000
        # print('seeds: ', len(self.seeds))
        for seed in self.seeds:
            loc = self.getLoc(int(seed))
            print(loc)
            if loc < smallest:
                smallest = loc
        return smallest

    def getSmallestRangeLoc(self):
        smallest = 100000000000
        # print('seeds: ', len(self.seeds))
        for seedPair in self.seeds:
            # print(seedPair)
            loc = self.getRangeLoc(seedPair)
            # print(loc)
            for locItem in loc: 
                if locItem < smallest:
                    smallest = locItem
        return smallest

def mapRangeValue(map, seedPair):
    seedRange = []
    mapRange = []
    for item in range(1, len(seedPair)+1):
        if(item % 2 == 0):
            idx = seedPair[item-1]
            seedRange.append([seed, idx])
        else:
            seed = seedPair[item-1]
            
    # Somehow Map each seedPair in the seedRange to the Map ... :/ 
    for pair in seedRange: 
        
        pairSrc = pair[0]
        pairCnt = pair[1]
        
        for mapLine in map: 
            dst = int(mapLine[0])
            src = int(mapLine[1])
            cnt = int(mapLine[2])
            
            srcDiff = pairSrc - src
            cntDiff = pairCnt - cnt
            
            # lowPair: the src, cnt for values less than src
            if(srcDiff < 0):
                lowPair = []
            
            # highPair: the src, cnt for values greater than src+cnt
            if((srcDiff + pairCnt) > 0):
                highPair = []
            
            # midPair: the src, cnt for values in the range of (src, src+cnt)
           if(srcDiff >= 0):
               # I'm too tired to keep doing this rn LOL 
               midPair = []
            
        
        
    
    return mapRange

def mapValue(map, value):
    dest = -1
    value = int(value)
    # print(value)
        
    for mapLine in map: 
        dst = int(mapLine[0])
        src = int(mapLine[1])
        cnt = int(mapLine[2])
        # print(dst, src, cnt)
        if value in range(src, (src+cnt)):
            idx = value - src
            # print('found a match:', value, 'in range:', src, '-', (src+cnt), 'at index:', idx)
            dest = dst + idx
            return int(dest)
    
    if dest == -1:
        dest = value       
         
    return int(dest)

def createSeedMap(content):
    # print('Seed Mapping')
    seeds = []
    allMaps = []
    currMap = []
    
    for line in content: 
        # print(len(line), line)
        input = line.split()
        # print(len(input) , input)
        if len(input) > 1 and input[0] == 'seeds:':
            # print('seed seeder')c
            for item in range(1, len(input)):
                if(item % 2 == 0):
                    idx = int(input[item])
                    seeds.append([seed, idx])
                else:
                    seed = int(input[item])
                
                
            # seeds = input[1:]
            # print(seeds)
        elif len(input) > 1 and input[-1] == 'map:': 
            # print('seed header')
            # print(len(line), line) 
            allMaps.append(currMap)               
            currMap = []
        elif len(input) > 2 and line == content[-1]:
            # print('seed value')
            # print(len(input), input)
            currMap.append(input)
            allMaps.append(currMap)
        elif len(input) > 2:
            # print('seed Value')
            # print(len(input), input)
            currMap.append(input)
        else:
            # print('seed spacer')
            continue
            
    
    allMaps = allMaps[1:]
    print(seeds)
    print(allMaps[0])
    return seedMap(seeds, allMaps[0], allMaps[1], allMaps[2], allMaps[3], allMaps[4], allMaps[5], allMaps[6])
    

# Part 1 Code
def part1(path):

    # Open the File
    content = openFile(path)
    seedMap = createSeedMap(content)
    print(seedMap.getSmallestLoc())
    
# Part 2 Code
def part2(path):
    
    # Open the File
    content = openFile(path)
    seedMap = createSeedMap(content)
    print(seedMap.getSmallestRangeLoc())
    
    
# Part 1 
# part1('input.txt')

# Part 2
part2('test2.txt')