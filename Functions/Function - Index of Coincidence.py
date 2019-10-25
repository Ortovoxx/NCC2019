#IoC - Index of Coincidence 

alphabetASCII = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
def convertToASCII(text): #Converts an array of characters into an array of their ASCII equivalent numbers
    perm = 0
    while perm < len(text): #goes through each array index and turns it from Character to ASCII
        text[perm] = ord(text[perm])
        perm = perm + 1
    return text
def removePunctuation(plain): #Removes punctuation
    plainText = plain.lower() 
    characters = list(plainText)
    charactersNoSymbol = []
    n = 0
    while n < len(characters):
        if ord(characters[n]) > 96 and ord(characters[n]) < 123 or ord(characters[n]) == 32: # 97 = A 122 = Z 32 = [SPACE]
            charactersNoSymbol.append(characters[n])
        n = n + 1
    charactersNoSymbolJoint = "".join(charactersNoSymbol)
    return charactersNoSymbolJoint
def removeSpaces(plain): #Removes spaces
    plainText = plain.lower()
    characters = list(plainText)
    charactersNoSpace = []
    n = 0
    while n < len(characters):
        if ord(characters[n]) != 32: # 32 ASCII for space
            charactersNoSpace.append(characters[n])
        n = n + 1
    charactersNoSpaceJoint = "".join(charactersNoSpace)
    return charactersNoSpaceJoint

##################################################################################################################

def indexOfCoincidence(text): #String input to calculate the Index of Coincidence of a text
    def letter(letterCount,textLength):
        letterValue = (letterCount / textLength)*((letterCount - 1)/(textLength - 1))
        return letterValue
    IoCARRAY = []
    alphaIndex = 0
    textArray = convertToASCII(list(removeSpaces(removePunctuation(text))))
    textLength = len(textArray)
    while alphaIndex < len(alphabetASCII):
        letterCount = textArray.count(alphaIndex+97)
        IoCARRAYStore = (letter(letterCount,textLength))
        IoCARRAY.append(IoCARRAYStore)
        alphaIndex = alphaIndex + 1
    IoC = sum(IoCARRAY)
    return IoC


user = input("text: ")
print(indexOfCoincidence(user))