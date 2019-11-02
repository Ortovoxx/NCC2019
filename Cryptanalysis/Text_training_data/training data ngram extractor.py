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


quadramDitionaryEnglish = {}
index = 0
os.chdir("/Users/Euan/Desktop") #Change to your local directory which contains this file, the training data .txt file and the output .txt file
with open("training_text.txt", "r") as f: #ENSURE THIS FILE NAME IS CORRECT OTHERWISE IT WILL ERROR!!!!!!!!
    dataUnformatted = f.read()
    quadramData = list(removeSpaces(removePunctuation(dataUnformatted)))
    quadramDitionaryEnglish = {}
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
        if quad in quadramDitionaryEnglish:
            quadramDitionaryEnglish[quad] = quadramDitionaryEnglish[quad] + 1
        else:
            quadramDitionaryEnglish[quad] = 1
        index = index + 1
    with open("ngram_output.txt", "w") as f:
        for n in quadramDitionaryEnglish:
            probability = quadramDitionaryEnglish[n] / len(quadramDitionaryEnglish) #calculates the probability of an ngram occuring
            f.writelines(n + " ") #the ngram
            f.writelines(str(probability) + "\n") #the probability of an ngram occuring
''' #Optional code to make another file with just the counts and not the probabilities
    with open("ngram_output_counts.txt", "w") as f:
        for n in quadramDitionaryEnglish:
            f.writelines(n + " ") #the ngram
            f.writelines(str(quadramDitionaryEnglish[n]) + "\n") #the number of occurances
'''
