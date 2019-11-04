from pycipher import SimpleSubstitution as SimpleSub
import random
import re
import os
import math

######## ALPHABET LISTS ########
alphabetASCII = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
alphabetCHARACTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#IN %
englishLetterFrequency = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]
englishLetterFrequencySorted = [12.702,9.056,8.167,7.507,6.966,6.749,6.327,6.094,5.987,4.253,4.025,2.782,2.758,2.406,2.360,2.228,2.015,1.974,1.929,1.492,0.978,0.772,0.153,0.150,0.095,0.074]
#Probabilty /1
englishLetterFrequencyProbability = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]
#The above array numbers map to the following letters (in order) -- e t a o i n s h r d l c u m w f g y p b v k j x q z
def search(itemToCheckFor,listToSearchFrom): #LINEAR SEARCH GLOBAL FUNCTION - Searches to see if there are repeats for random and keyword keys
    position = 0
    found = False
    while position < len(listToSearchFrom) and not found:
        if listToSearchFrom[position] == itemToCheckFor:
            found = True
        position += 1
    return found
def convertToASCII(textArray): #Converts an array of characters into an array of their ASCII equivalent numbers
    index = 0
    while index < len(textArray): #goes through each array index and turns it from Character to ASCII
        textArray[index] = ord(textArray[index])
        index += 1
    return textArray
def convertToCHARACTER(textArray): #Converts an array of ASCII equivalent numbers into an array of their ASCII equivalent characters
    index = 0
    while index < len(textArray): #goes through each array index and turns it from ASCII number to Character
        textArray[index] = chr(textArray[index])
        index += 1
    return textArray
def removePunctuation(string): #Removes punctuation from a string input
    plainText = string.lower() 
    characters = list(plainText)
    charactersNoSymbol = []
    index = 0
    while index < len(characters):
        if ord(characters[index]) > 96 and ord(characters[index]) < 123 or ord(characters[index]) == 32: # 97 = A 122 = Z 32 = [SPACE]
            charactersNoSymbol.append(characters[index])
        index += 1
    charactersNoSymbolJoint = "".join(charactersNoSymbol)
    return charactersNoSymbolJoint
def removeSpaces(string): #Removes spaces from a string input
    plainText = string.lower()
    characters = list(plainText)
    charactersNoSpace = []
    index = 0
    while index < len(characters):
        if ord(characters[index]) != 32: # 32 ASCII for space
            charactersNoSpace.append(characters[index])
        index += 1
    charactersNoSpaceJoint = "".join(charactersNoSpace)
    return charactersNoSpaceJoint
def loadEnglishNgram(): #loads a ngram file to a python ditionary
        os.chdir("/Users/Euan/Desktop/NCC2019/Cryptanalysis/Text_training_data") #path of ngram file to load make sure .txt file is in this folder MAKE SURE NGRAMS ARE LOWER CASE
        quadramDitionaryEnglish = {}
        index = 0
        with open("ngram_output.txt", "r") as f:
            quadramData = f.read()
            quadramArray = quadramData.split()
            while index < len(quadramArray):
                quadramDitionaryEnglish[quadramArray[index]] = float(quadramArray[index + 1])
                index += 2
        return quadramDitionaryEnglish
ngramDitionaryEnglish = loadEnglishNgram()
def ngramFitness(userCiperText,ngramDitionaryEnglish):
    def ngramExtraction(userCiperText): #Finds quadgrams from a ciphertext
        cipherText = list(removeSpaces(removePunctuation(userCiperText)))
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
    final = sum(logAB)
    return final
def substitionKeyCipher(userCipherText,userKey): #maps a ciphertext to plaintext according to the key given to it
    cipherText = convertToASCII(list(userCipherText)) #Converting cipher to numbers
    key = convertToASCII(list(userKey)) #Converting key to numbers
    def switchChar(cipherChar): #Switches a single character from its chiphertext to its plaintext
        alphaPerm = 0
        newChar = 0
        while alphaPerm < len(alphabetASCII): #as it goes through a letter it changes it 
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
def randomKey(): #generates a random key
    perms = 0
    key = []
    while perms < len(alphabetASCII): #Ensures 26 letters in the alphabet
        randomNo = random.randint(97, 122)
        repeat = search(randomNo,key) #Ensures each letter is unique
        if repeat == False:
            key.append(randomNo)
            perms += 1
    finalKey = "".join(convertToCHARACTER(key))
    return finalKey

#fitness = ngram_score('quadgrams.txt') # load our quadgram statistics

cipherText = "pmpafxaikkitprdsikcplifhwceigixkirradfeirdgkipgigudkcekiigpwrpucikceiginasikwduearrxiiqepcceindgmieinpwdfprduppcedoikiqiasafmfddfipfgmdafmfdteiki"
cipherText = "rbo rpktigo vcrb bwucja wj kloj hcjd km sktpqo cq rbwr loklgo vcgg cjqcqr kj skhcja wgkja wjd rpycja rk ltr rbcjaq cj cr"
cipherText = re.sub("[^A-Z]","",cipherText.upper()) #replaces anythin other than the upper case alphabet with "" and converts to uppercase

maxKey = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
maxScore = -99e9
parentScore,parentKey = maxScore,maxKey#[:]
# keep going until we are killed by the user
i = 0
while True == True:
    i += 1
    #random.shuffle(parentkey)
    parentKey = list(randomKey().upper())
    deciphered = substitionKeyCipher(cipherText,"".join(parentKey))
    parentScore = ngramFitness(deciphered,ngramDitionaryEnglish)
    count = 0
    while count < 1000:
        a = random.randint(0,25)
        b = random.randint(0,25)
        childKey = parentKey[:]
        # swap two characters in the child
        childKey[a],childKey[b] = childKey[b],childKey[a]
        deciphered = substitionKeyCipher(cipherText,"".join(childKey))
        childScore = ngramFitness(deciphered,ngramDitionaryEnglish)
        # if the child was better, replace the parent with it
        if childScore > parentScore:
            parentScore = childScore
            parentKey = childKey[:]
            count = 0
        count += 1
    # keep track of best score seen so far
    if parentScore > maxScore:
        maxScore,maxKey = parentScore,parentKey[:]
        print ("\nbest score so far:",maxScore,"on iteration",i)
        ss = SimpleSub(maxKey)
        print ("    best key: "+"".join(maxKey))
        print ("    plaintext: "+ ss.decipher(cipherText))
