import os
def removeSpaces(string): #Removes spaces from a string input
    plainText = string.lower()
    characters = list(plainText)
    charactersNoSpace = []
    index = 0
    while index < len(characters):
        if ord(characters[index]) != 32: # 32 ASCII for space
            charactersNoSpace.append(characters[index])
        index = index + 1
    charactersNoSpaceJoint = "".join(charactersNoSpace)
    return charactersNoSpaceJoint
def removePunctuation(string): #Removes punctuation from a string input
    plainText = string.lower() 
    characters = list(plainText)
    charactersNoSymbol = []
    index = 0
    while index < len(characters):
        if ord(characters[index]) > 96 and ord(characters[index]) < 123 or ord(characters[index]) == 32: # 97 = A 122 = Z 32 = [SPACE]
            charactersNoSymbol.append(characters[index])
        index = index + 1
    charactersNoSymbolJoint = "".join(charactersNoSymbol)
    return charactersNoSymbolJoint



os.chdir("/Users/Euan/Desktop/NCC2019/Cryptanalysis/textCorpus")
f = open("englishQuadgrams.txt", "w")
quadramDitionaryEnglish = {}
index = 0
with open("corpus.txt", "r") as f:
    dataUnformatted = f.read()
    quadramData = list(removeSpaces(removePunctuation(dataUnformatted)))
    quadramDitionaryCiphertext = {}
    index = 0
    n = 4 # the n in ngram -  change to 2 for bigrams and 3 for trigrams etc
    while index < len(quadramData) - (n - 1):
        quadIndex = 0
        singleQuadgram = []
        while quadIndex < n and index < len(quadramData):
            if index + quadIndex < len(quadramData):
                quaterQuadgramChar = quadramData[index + quadIndex]
                singleQuadgram.append(quaterQuadgramChar)
                quadIndex = quadIndex + 1
        quad = "".join(singleQuadgram)
        if quad in quadramDitionaryCiphertext:
            quadramDitionaryCiphertext[quad] = quadramDitionaryCiphertext[quad] + 1
        else:
            quadramDitionaryCiphertext[quad] = 1
        index = index + 1
    for x in quadramDitionaryCiphertext:
        f.write(x)
        f.write(str(quadramDitionaryCiphertext[x]))
