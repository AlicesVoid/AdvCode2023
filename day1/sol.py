# Dictionary with Words of Numbers to their Actual Values
numWords = {"one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "zero": 0}

def firstLastNumWord(line):
    
    # Establish Variables
    firstNum = ""
    lastNum = ""
    
    # Find a NumWord in the line 
    for word in numWords:
        if word in line:
                                     
            # If first and last are blank, set them both to word 
            if firstNum == "" and lastNum == "":

                firstNum = word
                lastNum = word
                        
            # Find how close the word is to the beginning of the line
            if line.find(word) < line.find(firstNum):

                firstNum = word
            
            # Find how close the word is to the end of the line 
            if line.rfind(word) > line.rfind(lastNum):
                lastNum = word         
                
            # print(word ,line.find(word), line.find(firstNum), line.rfind(lastNum))           

    
    # if firstNum != "" and lastNum != "":
        
    #     # Create #num# from num 
    #     fullFirst = str(numWords[firstNum]) + firstNum + str(numWords[firstNum])
    #     fullLast = str(numWords[lastNum]) + lastNum + str(numWords[lastNum])
        
    #     # Replace firstNum and lastNum with fullFirst and fullLast
    #     frontline = line.replace(firstNum, str(numWords[firstNum]))
    #     backline = line.replace(lastNum, str(numWords[lastNum]))   
        
    #     line = frontline + backline   
               
    # Return Line
    return [firstNum, lastNum]

def wordNumSum(line):

            # Find First and Last WordNum in line
            words = firstLastNumWord(line)
            
            # Check if there is a number in line
            if any(char.isdigit() for char in line):
                # Find First and Last Number in Line
                nums = ''.join(x for x in line if x.isdigit())
                num1 = nums[0]
                num2 = nums[-1]
                
                # print(num1, line.find(num1))
                # print(num2, line.rfind(num2))
                # print(words[0], line.find(words[0]))
                # print(words[-1], line.rfind(words[-1]))
                
                # Find how close the word is to the beginning of the line
                if words[0] != '' and words[-1] != '':
                    if line.find(words[0]) < line.find(nums[0]):

                        num1 = numWords[words[0]]
                        
                    # Find how close the word is to the beginning of the line
                    if line.rfind(words[-1]) > line.rfind(nums[-1]):

                        num2 = numWords[words[-1]]
            else:
                if words[0] != '' and words[-1] != '':
                    num1 = numWords[words[0]]
                    num2 = numWords[words[-1]]
                
            trueNum = str(num1) + str(num2)
            
            return int(trueNum)
            
            

def numSum (line):
    
           # Find Numbers in Line
            nums = ''.join(x for x in line if x.isdigit())

            # Combine Em into the Num
            num = nums[0] + nums[-1]
            
            # Return the Num 
            return int(num)

def part1(path):
    # Assert Total
    total = 0

    # Read Each Line of Input.txt
    with open(path) as f:
        content = f.readlines()
        
        # Loop through each line
        for line in content:
            
            total += numSum(line)
            
        # Print Total 
        print(total)    

# Same as Part 1 but looking for Entire Words instead of Numbers
def part2(path):
    
    # Assert Total 
    total = 0
    
    # Read Each Line of Input.txt
    with open(path) as f:
        content = f.readlines()
        
        for line in content:
            
            trueNum = wordNumSum(line)
            print(trueNum)
            
            total += trueNum
            
    print(total)
    
# Part 1 
#part1('test1.txt')
#part1('input.txt')

# Part 2
#part2('test2.txt')
part2('input.txt')