#Chi squared analysis

englishLetterFrequencyProbability = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]
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

########################################################################################

def chiSquaredStat(text):
    def letter(realLetterCount,expectedLetterCount):
        letterValue = ((realLetterCount - expectedLetterCount)**2) / expectedLetterCount
        return letterValue
    chiSquaredARRAY = []
    alphaIndex = 0
    textArray = convertToASCII(list(removeSpaces(removePunctuation(text))))
    textLength = len(textArray)
    while alphaIndex < len(alphabetASCII): 
        realLetterCount = textArray.count(alphaIndex + 97)
        expectedLetterCount = textLength * englishLetterFrequencyProbability[alphaIndex] #Compares it against an english distribution
        chiSquaredARRAYStore = letter(realLetterCount,expectedLetterCount)
        chiSquaredARRAY.append(chiSquaredARRAYStore)
        alphaIndex = alphaIndex + 1
    chiSquared = sum(chiSquaredARRAY)
    return chiSquared


while True == True:
    user = input("text: ")
    print(chiSquaredStat(user))
