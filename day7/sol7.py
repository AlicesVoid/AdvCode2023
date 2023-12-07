# Dictionary to Determine the Value of Each Card
cardValues = {'2': 1,
                '3': 2,
                '4': 3,
                '5': 4,
                '6': 5,
                '7': 6,
                '8': 7,
                '9': 8,
                'T': 9,
                'J': 10,
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

    # Show the Hand
    def showHand(self):
        return self.cards
    
    # Show the Bid 
    def showBid(self):
        return self.bid
    
    # Determine if the Hand has 5 of a kind
    def isFiveOfAKind(self):
        return len(set(self.cards)) == 1
    
    # Determine if the Hand has 4 of a kind
    def isFourOfAKind(self):
        if(len(set(self.cards)) == 2):
            
            # If commonChar == 4, return true
            if(commonChar(self.cards) == 4):
                return True
        
        return False
    
    # Determineif the Hand is a Full House 
    def isFullHouse(self):
        return len(set(self.cards)) == 2
    
    # Determine if the Hand has 3 of a kind
    def isThreeOfAKind(self):
        if(len(set(self.cards)) == 3):
                
            # If commonChar == 3, return true
            if(commonChar(self.cards) == 3):
                return True
                
                
                
        return False
    
    # Determine if the Hand has Two Pairs in it 
    def isTwoPair(self):
        return len(set(self.cards)) == 3
    
    # Determine if the Hand has One Pair in it 
    def isOnePair(self):
        return len(set(self.cards)) == 4
                
    # Determine if the Hand has a High Card
    def highCard(self):
        return len(set(self.cards)) == 5
    
    # Determine Which Hand the Player has
    def determineHand(self):
        if(self.isFiveOfAKind()):
            return "Five of a Kind"
        elif(self.isFourOfAKind()):
            return "Four of a Kind"
        elif(self.isFullHouse()):
            return "Full House"
        elif(self.isThreeOfAKind()):
            return "Three of a Kind"
        elif(self.isTwoPair()):
            return "Two Pair"
        elif(self.isOnePair()):
            return "One Pair"
        elif(self.highCard()):
            return "High Card"

# Parse the determienHand to determine if the hand is better than the other hand
def compHands(hand1, hand2):
    # For Both Hands, Run Determine Hand  
    for i in range(0, len(hand1)):
        # If the Hand is Better than the Other Hand
        if(handValues[hand1[i].determineHand()] < handValues[hand2[i].determineHand()]):
            print(hand1[i].determineHand(), ' beats ', hand2[i].determineHand())
            return hand1
        # If the Other Hand is Better than the Hand
        elif(handValues[hand1[i].determineHand()] > handValues[hand2[i].determineHand()]):
            print(hand2[i].determineHand(), ' beats ', hand1[i].determineHand())
            return hand2
        # If the Hands are Equal
        elif(handValues[hand1[i].determineHand()] == handValues[hand2[i].determineHand()]):
            return compCards(hand1, hand2)
    

# Determine which Hand is Stronger if They are Equal
def compCards(hand1, hand2):
    # For Both Hands, Iterate through the characters in the hand 
    for i in range(0, len(hand1)):
        # If the character in hand1 is greater than the character in hand2
        if(cardValues(hand1.showHand()[i]) > cardValues(hand2.showHand()[i])):
            print(hand1.showHand()[i], ' beats ', hand2.showHand()[i])
            return hand1
        # If the character in hand2 is greater than the character in hand1
        elif(cardValues(hand1.showHand()[i]) < cardValues(hand2.showHand()[i])):
            print(hand2.showHand()[i], ' beats ', hand1.showHand()[i])
            return hand2

def openFile(path):
    # Open File
    with open(path) as f:
        content = f.readlines()
        return content

# Part 1 Code
def part1(path):
    
    camelCards = []
    sortedCamelCards = []
    total = 0
    
    content = openFile(path)
    
    # Create a CamelCards Object for each line in the file
    for line in content: 
        # Split the Line 
        line = line.split()
        
        # Create a CamelCards Object for each line in the file
        camelCards.append(CamelCards(line[0], int(line[-1])))
    
    # Sort the Hands Based on How Good the Hands Are 
    for cards in camelCards:
        
        # If sortedCamelCards is empty, add the first hand to it
        if(len(sortedCamelCards) == 0):
            print(0, cards.showHand())
            sortedCamelCards.append(cards)
            
        # If sortedCamelCards is not empty, compare the hands and add them to the list
        else:
            # Loop Through the Camel Cards in the Sorted List and Figure out Which One it Beats 
            for i in range(0, len(sortedCamelCards)):
                # If the Hand is Better or Equal than the Other Hand
                if(handValues[cards.determineHand()] <= handValues[sortedCamelCards[i].determineHand()]):
                    sortedCamelCards.insert(i, cards)
                    break
                
                # If the Hand Value is Less, just keep Iterating
                elif(handValues[cards.determineHand()] > handValues[sortedCamelCards[i].determineHand()]):
                    continue
                
                # If there are no more hands in the list, add the hand to the end of the list
                else:
                    sortedCamelCards.append(cards)
                    break
    
    # Loop Through the Sorted Camel Cards and Determine the Payout 
    for i in range(0, len(sortedCamelCards)):
        # Total = Bid * (Length of sortedCamelCards + 1 - Index of Hand)
        print((len(sortedCamelCards) + 1 - (i + 1)), 'times ',sortedCamelCards[i].showBid())
        add2Total = sortedCamelCards[i].showBid() * (len(sortedCamelCards) + 1 - (i + 1))
        total += add2Total
    
    # Done
    print(total)
                    
# Part 2 Code
def part2(path):
    
    content = openFile(path)
    print(content)
    
# Part 1 
part1('test1.txt')

# Part 2
# part2('test2.txt')