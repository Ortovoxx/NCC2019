############# IMPORTANT INFO BEFORE USING THIS PROGRAM #############
# All functions should transfer data using lowercase no space no punctuation strings

#Modules to imports
import re

#==============================================================================================================================================================
#                                                                           TEXT MANIPULATION
#==============================================================================================================================================================

def BINtoDEC(self): # Binary to Decimal converter
    return int(str(self),2)
def DECtoBIN(self): # Decimal to Binary converter
    return int(re.sub("0b","",str(bin(self))))
def DECtoHEX(self): # Decimal to Hexadecimal converter
    return re.sub("0x","",str(hex(self)))
def HEXtoDEC(self): # Hexadecimal to Decimal converter
    return int(str(self),16)
def DECtoOCT(self): # Decimal to Octal converter
    return int(re.sub("0o","",str(oct(self))))
def OCTtoDEC(self): # Octal to Decimal converter
    return int(str(self),8)
def formatString(string): #removes everything apart from a-z lower case from a string
    return "".join(re.findall("[a-z]",string))
def reverseString(string): #Reverses the text
    return string[::-1]
def spliting(string,separator): # Returns a list from a string which has been split with a set separator
    return re.split(separator,string)
def convertToASCII(textList): #Converts an list of characters into an list of their ASCII equivalent numbers
    output = []
    for n in textList: #goes through each list index and turns it from Character to ASCII
        output.append(ord(n))
    return output
def convertToCHARACTER(textList): #Converts an list of ASCII equivalent numbers into an list of their ASCII equivalent characters
    output = []
    for n in textList: #goes through each list index and turns it from ASCII number to Character
        output.append(chr(n))
    return output
def search(itemToCheckFor,listToSearchFrom): #LINEAR SEARCH GLOBAL FUNCTION - Searches to see if there are repeats for random and keyword keys returns T or F
    position = 0
    found = False
    while position < len(listToSearchFrom) and not found:
        if listToSearchFrom[position] == itemToCheckFor:
            found = True
        position += 1
    return found
def shiftRight(listToMove,numberToMoveBy): # Shifts a list one place to the right including wrap arrounds
    index = 0
    while index < numberToMoveBy:
        position = listToMove.pop()
        listToMove.insert(0, position)
        index += 1
    return listToMove
def addPadding(cipher,key): # pads a transposition ciphertext with a padding character of X
    cipher = list(cipher)
    lengthCipher = len(cipher)
    remainder = lengthCipher % key # Finds how many padding characters to add
    if remainder == 0: #If the ciphertext length is divisible by the key perfectly then no padding is needed
        return "".join(cipher)
    else:
        addPad = 0
        while addPad <= remainder: # Loops round the cipher text array adding a padding character each time
            cipher.append("x") # The padding character
            addPad+=1
        return "".join(cipher)
def textBlock(textIN): #Takes a plaintext string input and returns a list with a sublist of blocked characters
    n = 3 #The size of the text blocks
    text = list(textIN)
    length = len(text)
    blockedText = []
    remainder = length % n
    index = addPad = 0
    if remainder != 0:
        while addPad <= remainder: # Loops round the cipher text array adding a padding character each time
            text.append("x") # The padding character
            addPad+=1
    while index < length:
        blocked = []
        blocking = 0
        while blocking < n:
            add = text[blocking + index]
            blocked.append(add)
            blocking+=1
        blockedText.append("".join(blocked))
        index+=n
    return blockedText
def textReplace(textBlockIN,find,replace):#Takes an array with strings of blocked characters and repalces them with others
    textBlockOUT = []
    for n in textBlockIN:
        new = n.replace(find,replace)
        textBlockOUT.append(new)
    return textBlockOUT
def factors(textIN): #finds the factors of a text
    text = list(textIN)
    length = len(text)
    factorList = [length]
    for i in range(1,length):
        if length % i == 0:
            factorList.append(int(i))
    return sorted(factorList)