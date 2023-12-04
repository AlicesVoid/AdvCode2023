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

def numWordToNum(line):
    
    # Establish Variables
    firstNum = ""
    lastNum = ""
    
    # Find the numWord closest to the front of the string 
    for numWord in numWords:
        if numWord in line:
            firstNum = numWord
            break
        
    # Find the numWord closest to the end of the string 
    for numWord in numWords:
        if numWord in line:
            lastNum = numWord
            break
    
        
    # Return Line
    return line

def part1():
    # Assert Total
    total = 0

    # Read Each Line of Input.txt
    with open('input.txt') as f:
        content = f.readlines()
        
        # Loop through each line
        for line in content:
            
            # Find First Number in Line
            nums = ''.join(x for x in line if x.isdigit())

            # Combine Em into the Num
            num = nums[0] + nums[-1]
            
            # Add Em Up
            total += int(num)
            
        # Print Total 
        print(total)    

# Same as Part 1 but looking for Entire Words instead of Numbers
def part2():
    
    # Assert Total 
    total = 0
    
    # Read Each Line of Input.txt
    with open('test2.txt') as f:
        content = f.readlines()
        
        for line in content:
            
            numLine = numWordToNum(line);
            print(numLine)
    
    
    return 0
    


    
# Part 1 
#part1()

# Part 2
part2()