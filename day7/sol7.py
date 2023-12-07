# Dictionary to Determine the Value of Each Card (J is now the Weakest Card)
cardValues = {'J': 1,
              '2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9,
                'T': 10,
                'Q': 11,
                'K': 12,
                'A': 13}

# Dictionary to Determine the Value of Each Hand
handValues = {'Five of a Kind': 1,
                'Four of a Kind': 2,
                'Full House': 3,
                'Three of a Kind': 4,
                'Two Pair': 5,
                'One Pair': 6,
                'High Card': 7}

# Function to Find the Number of the Most Common Character in a String 
def commonChar(String):
    # Create a Dictionary to Store the Number of Each Character
    charDict = {}
    
    # Loop Through the String and Add the Characters to the Dictionary
    for char in String:
        # If the Character is Already in the Dictionary, Increment the Value
        if(char in charDict):
            charDict[char] += 1
        # If the Character is Not in the Dictionary, Add it to the Dictionary
        else:
            charDict[char] = 1
    
    # Find the Maximum Value in the Dictionary
    maxVal = max(charDict.values())
    
    # Find the Key that Corresponds to the Maximum Value
    for key in charDict:
        if(charDict[key] == maxVal):
            return key

# Create Class "CamelCards" with a string 
class CamelCards:
   
    # Constructor
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.hand = self.determineHand()
        self.high = self.highTotal()
        self.hand_j = self.swapForJ()

    # Show the Hand
    def showCards(self):
        return self.cards
    
    # Show the Bid 
    def showBid(self):
        return self.bid
    
    # Show the Hand 
    def showHand(self):
        return self.hand
    
    # Shows the J Hand 
    def showHandJ(self):
        return self.hand_j
    
    # Show the highCard Number
    def showHighCard(self):
        return self.high
    
    # Finds Five Numbers for the Card Values
    def highTotal(self):
        highCard = []
        # For Each Character in self.cards, get the value of the card
        for i in range(0, len(self.cards)):
            highCard.append(cardValues[self.cards[i]])
        return highCard
    
    # Determines the Hand of the User
    def determineHand(self):
        # Create a Dictionary to Store the Number of Each Character
        charDict = {}
        
        # Loop Through the String and Add the Characters to the Dictionary
        for char in self.cards:
            # If the Character is Already in the Dictionary, Increment the Value
            if(char in charDict):
                charDict[char] += 1
            # If the Character is Not in the Dictionary, Add it to the Dictionary
            else:
                charDict[char] = 1
        
        # Find the Maximum Value in the Dictionary
        #print(charDict)
        
        maxVal = max(charDict.values())
        
        # Find the Key that Corresponds to the Maximum Value
        for key in charDict:
            if(charDict[key] == maxVal):
                # If the Maximum Value is 5, Return Five of a Kind
                if(maxVal == 5):
                    return 'Five of a Kind'
                # If the Maximum Value is 4, Return Four of a Kind
                elif(maxVal == 4):
                    return 'Four of a Kind'
                # If the Maximum Value is 3, Return Three of a Kind
                elif(maxVal == 3):
                    # If the Hand is a Full House, Return Full House
                    if(2 in charDict.values()):
                        return 'Full House'
                    # If the Hand is a Three of a Kind, Return Three of a Kind
                    else:
                        return 'Three of a Kind'
                # If the Maximum Value is 2, Return Two Pair
                elif(maxVal == 2):
                    # Check that the Dict has 2 Values of 2
                    if(list(charDict.values()).count(2) == 2):
                        return 'Two Pair'
                    # If the Hand is a One Pair, Return One Pair
                    else:
                        return 'One Pair'
                # If the Maximum Value is 1, Return High Card
                elif(maxVal == 1):
                    return 'High Card'

    # Swaps out J for the Best Card 
    def swapForJ(self):
         # Create a Dictionary to Store the Number of Each Character
        charDict = {}
        Jtotal = 0
        
        # Loop Through the String and Add the Characters to the Dictionary
        for char in self.cards:
            # Make sure it's not J
            if(char != 'J'):
                # If the Character is Already in the Dictionary, Increment the Value
                if(char in charDict):
                    charDict[char] += 1
                # If the Character is Not in the Dictionary, Add it to the Dictionary
                else:
                    charDict[char] = 1
            else: 
                Jtotal += 1
                
        # If the charDict contains J, get the Jtotal 
        if(Jtotal > 0):
            
            # Bounds-Checking
            if(Jtotal == 5):
                return 'Five of a Kind'
            
            # Add the Jtotal to the highest value in charDict 
            for key in charDict:
                if(charDict[key] == max(charDict.values())):
                    charDict[key] += Jtotal
                    break
            
            # If there's no highest value in charDict, add Jtotal to the highest card value 
            if(max(charDict.values()) == 1):
                # Find the Key with the Highest Card Value 
                maxKey = max(charDict, key=charDict.get)
                # Add the Jtotal to the Highest Card Value
                charDict[maxKey] += Jtotal
        
        # Find the Maximum Value in the Dictionary
        #print(charDict)
        print(self.cards, charDict)
        maxVal = max(charDict.values())
        
        # Find the Key that Corresponds to the Maximum Value
        for key in charDict:
            if(charDict[key] == maxVal):
                # If the Maximum Value is 5, Return Five of a Kind
                if(maxVal == 5):
                    return 'Five of a Kind'
                # If the Maximum Value is 4, Return Four of a Kind
                elif(maxVal == 4):
                    return 'Four of a Kind'
                # If the Maximum Value is 3, Return Three of a Kind
                elif(maxVal == 3):
                    # If the Hand is a Full House, Return Full House
                    if(2 in charDict.values()):
                        return 'Full House'
                    # If the Hand is a Three of a Kind, Return Three of a Kind
                    else:
                        return 'Three of a Kind'
                # If the Maximum Value is 2, Return Two Pair
                elif(maxVal == 2):
                    # Check that the Dict has 2 Values of 2
                    if(list(charDict.values()).count(2) == 2):
                        return 'Two Pair'
                    # If the Hand is a One Pair, Return One Pair
                    else:
                        return 'One Pair'
                # If the Maximum Value is 1, Return High Card
                elif(maxVal == 1):
                    return 'High Card'
        

# Parse the determienHand to determine if the hand is better than the other hand
def compHands(hand1, hand2):
    # If the Hand Values are Equal, Compare the High Card
    if(handValues[hand1.showHand()] == handValues[hand2.showHand()]):
        return compCards(hand1, hand2)
    # If the Hand Values are Not Equal, Compare the Hand Values
    else:
        # If the Hand Value of hand1 is Greater, Return hand1
        if(handValues[hand1.showHand()] < handValues[hand2.showHand()]):
            return hand1
        # If the Hand Value of hand2 is Greater, Return hand2
        else:
            return hand2
        
# Parse the determienHand to determine if the hand is better than the other hand
def compHandsJ(hand1, hand2):
    # If the Hand Values are Equal, Compare the High Card
    if(handValues[hand1.showHandJ()] == handValues[hand2.showHandJ()]):
        return compCards(hand1, hand2)
    # If the Hand Values are Not Equal, Compare the Hand Values
    else:
        # If the Hand Value of hand1 is Greater, Return hand1
        if(handValues[hand1.showHandJ()] < handValues[hand2.showHandJ()]):
            return hand1
        # If the Hand Value of hand2 is Greater, Return hand2
        else:
            return hand2
    
# Determine which Hand is Stronger if They are Equal
def compCards(hand1, hand2):
    # Iterate through the high card lists and figure out which one is greater
    for i in range(0, len(hand1.showHighCard())):
        # If the Card Value of hand1 is Greater, Return hand1
        if(hand1.showHighCard()[i] > hand2.showHighCard()[i]):
            return hand1
        # If the Card Value of hand2 is Greater, Return hand2
        elif(hand1.showHighCard()[i] < hand2.showHighCard()[i]):
            return hand2
        # If the Card Value of hand1 is Equal to hand2, Continue
        else:
            continue

# Open the File and Return the Content
def openFile(path):
    # Open File
    with open(path) as f:
        content = f.readlines()
        return content

# Part 1 Code
def part1(path):
    
    camelCards = []
    total = 0
    
    content = openFile(path)
    
    # Create a CamelCards Object for each line in the file
    for line in content: 
        # Split the Line 
        line = line.split()
        
        # Create a CamelCards Object for each line in the file
        newCard = CamelCards(line[0], int(line[-1]))
        
        # Super Ultra Mega Debugging
        print(newCard.showCards(), newCard.showBid(), newCard.showHand(), newCard.showHighCard())
        
        # If CamelCards is Empty, Add the Card to the List
        if(len(camelCards) == 0):
            camelCards.append(newCard)
        else:
            # Iterate Through the List of CamelCards
            for i in range(0, len(camelCards)): 
                # if compHands returns the newCard, add the newCard to the List
                if(compHands(newCard, camelCards[i]) == newCard):
                    camelCards.insert(i, newCard)
                    break
                # If at the end of the list, just append the newCard
                elif(i == len(camelCards)-1):
                    camelCards.append(newCard)
                    break
    
    # Get the Total Earned
    for i in range(0, len(camelCards)):
        # Total Earned = Bid * (Number of Cards - Position in List)
        addVal = camelCards[i].showBid() * (len(camelCards) - i)
        total += addVal
        
    # Done
    print(total)
                    
# Part 2 Code
def part2(path):
    
    
    camelCards = []
    total = 0
    
    content = openFile(path)
    
    # Create a CamelCards Object for each line in the file
    for line in content: 
        # Split the Line 
        line = line.split()
        
        # Create a CamelCards Object for each line in the file
        newCard = CamelCards(line[0], int(line[-1]))
        
        # Super Ultra Mega Debugging
        # print(newCard.showCards(), newCard.showBid(), newCard.showHandJ(), newCard.showHighCard())
        
        # If CamelCards is Empty, Add the Card to the List
        if(len(camelCards) == 0):
            camelCards.append(newCard)
        else:
            # Iterate Through the List of CamelCards
            for i in range(0, len(camelCards)): 
                # if compHands returns the newCard, add the newCard to the List
                if(compHandsJ(newCard, camelCards[i]) == newCard):
                    camelCards.insert(i, newCard)
                    break
                # If at the end of the list, just append the newCard
                elif(i == len(camelCards)-1):
                    camelCards.append(newCard)
                    break
    
    # Get the Total Earned
    for i in range(0, len(camelCards)):
        # Total Earned = Bid * (Number of Cards - Position in List)
        addVal = camelCards[i].showBid() * (len(camelCards) - i)
        total += addVal
        
    # Done
    print(total)
    
# Part 1 
# part1('input.txt')

# Part 2
part2('input.txt')