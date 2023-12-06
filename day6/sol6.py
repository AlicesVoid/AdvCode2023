def openFile(path):
    # Open File
    with open(path) as f:
        content = f.readlines()
        return content

def boat_dist(t_max, t_press):
    d = (t_max - t_press)*t_press
    return d

def beat_record(time, record):
    records = 0;
    # loop from 1 to time 
    for i in range(1, time):
        # if beat record
        if boat_dist(time, i) > record:
            records += 1

    return records

# Part 1 Code
def part1(path):

    times = []
    dists = []
    total = 1
    
    # Open File 
    content = openFile(path)

    for line in content:
        words = line.split()
        
        # If the first value is time, store every subsequent value as an integer in times
        if words[0] == 'Time:':
            for word in words[1:]:
                times.append(int(word))
    
        # If the first value is distance, store every subsequent value as an integer in dists
        elif words[0] == 'Distance:':
            for word in words[1:]:
                dists.append(int(word))
        
    # Loop from 1 to the length of times
    for i in range(0, len(times)):
        # If the boat beats the record, print the time
        records = beat_record(times[i], dists[i])
        print(records)
        total *= records
             
    print(total)
   
# Part 2 Code
def part2(path):
    
    times = []
    dists = []
    realtime = ''
    realdist = ''
    total = 1
    
    # Open File 
    content = openFile(path)

    for line in content:
        words = line.split()
        
        # If the first value is time, store every subsequent value  in times
        if words[0] == 'Time:':
            for word in words[1:]:
                times.append(word)
                
        # If the first value is distance, store every subsequent value in dists
        elif words[0] == 'Distance:':
            for word in words[1:]:
                dists.append(word)
                
    # add all the values to the realtime and realdist
    for time in times:
        realtime += time
    for dist in dists:
        realdist += dist
    
    # print(times, dists)
    # print(realtime, realdist)

    records = beat_record(int(realtime), int(realdist))
    total *= records
             
    print(total)
    
# Part 1 
part1('test1.txt')

# Part 2
part2('test2.txt')
