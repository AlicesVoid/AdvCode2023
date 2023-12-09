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

# Part 1 Code
def part1(path):

    # Open File
    content = openFile(path)
    input = parseContent(content)
    print(input)
    

# Part 2 Code
def part2(path):
    
    # Open File
    content = openFile(path)
    input = parseContent(content)
    
# Part 1 
# part1('test1.txt')

# Part 2
# part2('test2.txt')