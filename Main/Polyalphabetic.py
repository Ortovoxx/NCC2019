#==============================================================================================================================================================
#                                                                  VARIABLES, CONSTANTS AND FORMATTING - DO NOT EDIT
#==============================================================================================================================================================

#Modules to imports
import random
import os
import math
import time
import re

############# IMPORTANT INFO BEFORE USING THIS PROGRAM #############
# Ensure you have an ngram.txt file in the correct directory:
loadEnglishNgramDirectory = "/Users/Euan/Desktop/NCC2019/Cryptanalysis/Text_training_data"
loadKeyWordsDirectory = "/Users/Euan/Desktop/NCC2019/Cryptanalysis"
outputFilesHere = "/Users/Euan/Desktop/NCC2019/Out"
# All functions should transfer data using lowercase no space no punctuation strings

#Menu and input formats
cipherSolverInputFormat = '''*************** CIPHERTEXT: **************
'''
textManipulationInputFormat = '''*********** INPUT YOUR TEXT: ***********
'''

######## ALPHABET LISTS ########
alphabetASCII = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
alphabetCHARACTER = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#all in expected % occurance
englishLetterFrequency = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]
englishLetterFrequencySorted = [12.702,9.056,8.167,7.507,6.966,6.749,6.327,6.094,5.987,4.253,4.025,2.782,2.758,2.406,2.360,2.228,2.015,1.974,1.929,1.492,0.978,0.772,0.153,0.150,0.095,0.074]
#The above list numbers map to the following letters (in order) -- e t a o i n s h r d l c u m w f g y p b v k j x q z

def loadEnglishNgram(): #loads a ngram file to a python ditionary
        os.chdir(loadEnglishNgramDirectory) #path of ngram file to load make sure .txt file is in this folder MAKE SURE NGRAMS ARE LOWER CASE
        quadramDitionaryEnglish = {}
        with open("ngram.txt", "r") as f:
            for line in f:
                quadramList = line.split()
                quadramDitionaryEnglish[quadramList[0]] = float(quadramList[1])
        return quadramDitionaryEnglish
def loadKeyWords(): #loads a keyword file to a python list
        os.chdir(loadKeyWordsDirectory) #path of ngram file to load make sure .txt file is in this folder MAKE SURE NGRAMS ARE LOWER CASE
        keyWords = []
        with open("keywords.txt", "r") as f:
            for line in f:
                keyWords.append(line.strip("\n"))
        return keyWords
def export(): #loads a ngram file to a python ditionary
    os.chdir(outputFilesHere) #path of ngram file to load make sure .txt file is in this folder MAKE SURE NGRAMS ARE LOWER CASE
    with open("output.txt", "a") as f:
        for key in outputExportDitionary:
            f.write(key +"\n")
            f.write(outputExportDitionary[key]+"\n")
keyWords = loadKeyWords()
ngramDitionaryEnglish = loadEnglishNgram()
outputExportDitionary = {}

#==============================================================================================================================================================
#                                                       TEXT MANIPULATION AND REPEATED USE FUNCTIONS - DO NOT EDIT
#==============================================================================================================================================================

def convertToASCII(textList): #Converts an list of characters into an list of their ASCII equivalent numbers
    index = 0
    while index < len(textList): #goes through each list index and turns it from Character to ASCII
        textList[index] = ord(textList[index])
        index += 1
    return textList
def convertToCHARACTER(textList): #Converts an list of ASCII equivalent numbers into an list of their ASCII equivalent characters
    index = 0
    while index < len(textList): #goes through each list index and turns it from ASCII number to Character
        textList[index] = chr(textList[index])
        index += 1
    return textList
def formatString(string): #removes everything apart from a-z lower case from a string
    noPunctuationList = re.findall("[a-z]",string)
    outputString = "".join(noPunctuationList)
    return outputString
def reverseString(string): #Reverses the text
    return string[::-1]
def search(itemToCheckFor,listToSearchFrom): #LINEAR SEARCH GLOBAL FUNCTION - Searches to see if there are repeats for random and keyword keys
    position = 0
    found = False
    while position < len(listToSearchFrom) and not found:
        if listToSearchFrom[position] == itemToCheckFor:
            found = True
        position += 1
    return found
def shiftRight(listToMove,numberToMoveBy):
    index = 0
    while index < numberToMoveBy:
        position = listToMove.pop()
        listToMove.insert(0, position)
        index += 1
    return listToMove
def substitionKeyCipher(userCipherText,userKey): #maps a ciphertext to plaintext according to the key given to it
    cipherText = convertToASCII(list(userCipherText)) #Converting cipher to numbers
    key = convertToASCII(list(userKey)) #Converting key to numbers
    def switchChar(cipherChar): #Switches a single character from its chiphertext to its plaintext
        alphaPerm = 0
        newChar = 0
        while alphaPerm < 26: #as it goes through a letter it changes it 
            if cipherChar == key[alphaPerm]:
                newChar = alphabetASCII[alphaPerm]
            alphaPerm += 1
        return newChar
    textPerm = 0
    switchedCipher = []
    while textPerm < len(cipherText): #Goes through each character one by one and sends to the function which converts cipher to plain
        switchedCipher.append(switchChar(cipherText[textPerm]))
        textPerm += 1
    switchedCipherStr = "".join(convertToCHARACTER(switchedCipher))
    return switchedCipherStr
def characterFrequency(encryptedText):
    frequencies = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in encryptedText: #iterates through each character in encrypted_cipher text
        index = 0 #element index set at 0 #WHEN data at index (character in encrypted text) does not equal first element #AND the alphabet index is less than 25, (i.e all letters encompassed only):
        while i != letter[index] and index < 25: #THEN increment pos index ++, avoids indexing greater than alphabet list
           if index <= 24:
               index += 1
        else: #increments relative index dependant upon character contained within i
            if i == letter[index]:
                frequencies[index] = frequencies[index] + 1 #if character in encrypted_text is a space,data @ alphabet[26] ++:       
    return frequencies
def characterFrequencyProbability(encryptedText):
    frequencies = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    probability = []
    for i in encryptedText: #iterates through each character in encrypted_cipher text
        index = 0 #element index set at 0 #WHEN data at index (character in encrypted text) does not equal first element #AND the alphabet index is less than 25, (i.e all letters encompassed only):
        while i != letter[index] and index < 25: #THEN increment pos index ++, avoids indexing greater than alphabet list
           if index <= 24:
               index += 1
        else: #increments relative index dependant upon character contained within i
            if i == letter[index]:
                frequencies[index] = frequencies[index] + 1 #if character in encrypted_text is a space,data @ alphabet[26] ++:
    for n in frequencies:
        x = round((n / len(encryptedText)),5)
        probability.append(x)
    return probability
def indexOfCoincidence(text): #String input to calculate the Index of Coincidence of a text
    def letter(letterCount,textLength):
        letterValue = (letterCount / textLength)*((letterCount - 1)/(textLength - 1))
        return letterValue
    IoCLIST = []
    alphaIndex = 0
    textList = convertToASCII(list(text))
    textLength = len(textList)
    while alphaIndex < 26:
        letterCount = textList.count(alphaIndex + 97)
        IoCLISTStore = (letter(letterCount,textLength))
        IoCLIST.append(IoCLISTStore)
        alphaIndex += 1
    return sum(IoCLIST)
def chiSquaredStat(text): #String input which calculates the chi-squared statistic of a text
    def letter(realLetterCount,expectedLetterCount):
        letterValue = ((realLetterCount - expectedLetterCount)**2) / expectedLetterCount
        return letterValue
    chiSquaredLIST = []
    alphaIndex = 0
    textList = convertToASCII(list(text))
    textLength = len(textList)
    while alphaIndex < 26: 
        realLetterCount = textList.count(alphaIndex + 97)
        expectedLetterCount = textLength * (englishLetterFrequency[alphaIndex]) / 100 #Compares it against an english distribution probability
        chiSquaredLISTStore = letter(realLetterCount,expectedLetterCount)
        chiSquaredLIST.append(chiSquaredLISTStore)
        alphaIndex += 1
    return sum(chiSquaredLIST)
def ngramFitness(userCiperText):
    def ngramExtraction(userCiperText): #Finds quadgrams from a ciphertext
        cipherText = list(userCiperText)
        quadramDitionaryCiphertext = {}
        index = 0
        n = 4 # the n in ngram -  change to 2 for bigrams and 3 for trigrams etc
        while index < len(cipherText) - (n - 1):
            quadIndex = 0
            singleQuadgram = []
            while quadIndex < n and index < len(cipherText):
                if index + quadIndex < len(cipherText):
                    quaterQuadgramChar = cipherText[index + quadIndex]
                    singleQuadgram.append(quaterQuadgramChar)
                    quadIndex += 1
            quad = "".join(singleQuadgram)
            if quad in quadramDitionaryCiphertext:
                quadramDitionaryCiphertext[quad] = quadramDitionaryCiphertext[quad] + 1
            else:
                quadramDitionaryCiphertext[quad] = 1
            index += 1
        return quadramDitionaryCiphertext
    quadramDitionaryCiphertext = ngramExtraction(userCiperText)
    logAB = []
    probQuadgram = 0
    for index in quadramDitionaryCiphertext:
        if index in ngramDitionaryEnglish:
            probQuadgram = ngramDitionaryEnglish[index]
            loggedProbQuadgram = math.log10(probQuadgram)
            logAB.append(loggedProbQuadgram)
        else:
            probQuadgram = 1e-50 #floors it as / 0 should be -infinity but that cannot be logged -- smaller this number bigger gap between english and non english
            loggedProbQuadgram = math.log10(probQuadgram)
            logAB.append(loggedProbQuadgram)
    return sum(logAB)
def relationToEnglishFrequency(cipherTextFrequency): # Finds the difference between a ciphertext frequency ( % ) and english frequency and outputs a score 
    index = 0
    lists = []
    while index < 25:
        difference = round(englishLetterFrequency[index] - (cipherTextFrequency[index])*100,10)
        lists.append(difference)
        index+=1
    score = sum(lists)
    return round(score,10)

#==============================================================================================================================================================
#                                                            CIPHER SOLVING - EDITABLE
#==============================================================================================================================================================
ciphertext = ""
key = "hello"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def decrypt(ciphertext,key):
    plaintext = ''
    for i in range(len(ciphertext)):
        fre  = len(key)
        gg = i%fre
        p = ALPHABET.index(ciphertext[i])
        k = ALPHABET.index(key[gg])
        c = (p - k) % 26
        plaintext += ALPHABET[c]
    return plaintext
key = ['']*3
for key[0] in ALPHABET:
    for key[1] in ALPHABET:
        for key[2] in ALPHABET:
            pt = decrypt(ciphertext,key)
            fit = ngramFitness(pt)
            if fit > -10:
                break
            else:
                continue
            break
        else:
            continue
    break
plaintext = decrypt(ciphertext,key)






#==============================================================================================================================================================
#                                                   USER INPUT / OUTPUT                   MAIN PROGRAM
#==============================================================================================================================================================

userKey = "abcdefghijklmnopqrstuvwxyz" #Sets a defult user key ~~~~WARNING~~~~ Wont show error if there is not a key generated as this one will take over ~~~~WARNING~~~~
keyIterations = REPLACEME123 = 0
exporting = False

#########  Turn each function on or off  #########

# KEY WORD:
vigStart = True

# DECLARE USERCIPHER HERE AND COMMENT OUT THE USER INPUT IF YOU ARE WORKING ON THE SAME CIPHER
userCipherNoFormatBypass = ""
userCipher = formatString((userCipherNoFormatBypass).lower())

while True: #Loops the entire program
    #userCipher = formatString((input(cipherSolverInputFormat)).lower()) # ensures all ciphertext given to functions is correclty formatted
    #########################################################
    #           Calling different deciphering functions
    #########################################################
    while keyIterations < keyIterations + 1:
        if vigStart == True: #Ceaser shifts done 26 times
            cipherOut = "test"
        ###############
        if exporting == True:
            export()
            print("exported!")
        keyIterations += 1
        #########################################################
        #                   Text statistics
        #########################################################
        ### Choose which scoring system you want to rank texts by: ###
        
        #indexOfCoincidenceText = round(indexOfCoincidence(cipherOut),10)
        #chiSquaredText = round(chiSquaredStat(cipherOut),10)
        #ngramScore = ngramFitness(cipherOut)
        #relationScore = relationToEnglishFrequency(characterFrequencyProbability(cipherOut))

        # if relationScore < 0.05 and relationScore > -0.05:
        ngramScore = -400
        if ngramScore > -40: # Change this number here the closer to 0 the less it will accept and print
            indexOfCoincidenceText = round(indexOfCoincidence(cipherOut),10)
            chiSquaredText = round(chiSquaredStat(cipherOut),10)
            ngramScore = ngramFitness(cipherOut)
            relationScore = relationToEnglishFrequency(characterFrequencyProbability(cipherOut))
            outputExportDitionary[userKey] = cipherOut
            cipherOutKeyOut ='''
================== PLAINTEXT: ==================
{printedCipherOut}
===================== KEY: =====================
{printedUserKey}
================= STATISTICS: ==================
Number of keys              {printedAttempts}
log Ngram Score             {printedNgramScore}
Index Of Coincidence        {printedIoC}
Chi Squared                 {printedChi}
English Frequency Relation  {printedRelationScore}
'''.format(printedCipherOut = cipherOut,printedUserKey = userKey,printedNgramScore = ngramScore,printedAttempts = keyIterations,printedIoC = indexOfCoincidenceText, printedChi = chiSquaredText,printedRelationScore = relationScore)
            print(cipherOutKeyOut)
