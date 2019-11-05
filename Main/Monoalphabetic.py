#==============================================================================================================================================================
#                                                                  VARIABLES, CONSTANTS AND FORMATTING - DO NOT EDIT
#==============================================================================================================================================================

#Modules to imports
import random
import os
import math
import time
import requests
import re

#Menu and input formats
cipherSolverInputFormat = '''*************** CIPHERTEXT: **************
'''
textManipulationInputFormat = '''*********** INPUT YOUR TEXT: ***********
'''

######## ALPHABET LISTS ########
alphabetASCII = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
alphabetCHARACTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#IN %
englishLetterFrequency = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]
englishLetterFrequencySorted = [12.702,9.056,8.167,7.507,6.966,6.749,6.327,6.094,5.987,4.253,4.025,2.782,2.758,2.406,2.360,2.228,2.015,1.974,1.929,1.492,0.978,0.772,0.153,0.150,0.095,0.074]
#Probabilty /1
englishLetterFrequencyProbability = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]
#The above array numbers map to the following letters (in order) -- e t a o i n s h r d l c u m w f g y p b v k j x q z

freqWords = ["the","of","to","and","a","in","is","it","you","that","he","was","for","on","are","with","as","i","his","they","be","at","one","have","this","from","or","had","by","hot","but","some","what","there","we","can",
             "out","other","were","all","your","when","up","use","word","how","said","an","each","she","which","do","their","time","if","will","way","about","many","then","them","would","write","like","so","these","her","long",
             "make","thing","see","him","two","has","look","more","day","could","go","come","did","my","sound","no","most","number","who","over","know","water","than","call","first","people","may","down","side","been","now",
             "any","new","work","part","take","get","place","made","live","where","after","back","little","only","round","man","year","came","show","every","good","me","give","our","under","name","very","through","just","form",
             "much","great","think","say","help","low","line","before","turn","cause","same","mean","differ","move","right","boy","old","too","does","tell","sentence","set","three","want","air","well","also","play","small","end",
             "put","home","read","hand","port","large","spell","add","even","land","here","must","big","high","such","follow","act","why","ask","men","change","went","light","kind","off","need","house","picture","try","again",
             "animal","point","mother","world","near","build","self","earth","father","head","stand","own","page","should","country","found","answer","school","grow","study","still","learn","plant","cover","food","sun","four",
             "thought","let","keep","eye","never","last","door","between","city","tree","cross","since","hard","start","might","story","saw","far","sea","draw","left","late","run","dont","while","press","close","night","real",
             "life","few","stop","open","seem","together","next","white","children","begin","got","walk","example","ease","paper","often","always","music","those","both","mark","book","letter","until","mile","river","car","feet",
             "care","second","group","carry","took","rain","eat","room","friend","began","idea","fish","mountain","north","once","base","hear","horse","cut","sure","watch","color","face","wood","main","enough","plain","girl",
             "usual","young","ready","above","ever","red","list","though","feel","talk","bird","soon","body","dog","family","direct","pose","leave","song","measure","state","product","black","short","numeral","class","wind",
             "question","happen","complete","ship","area","half","rock","order","fire","south","problem","piece","told","knew","pass","farm","top","whole","king","size","heard","best","hour","better","true","during","hundred",
             "am","remember","step","early","hold","west","ground","interest","reach","fast","five","sing","listen","six","table","travel","less","morning","ten","simple","several","vowel","toward","war","lay","against","find",
             "pattern","slow","center","love","person","money","serve","appear","road","map","science","rule","govern","pull","cold","notice","voice","fall","power","town","fine","certain","fly","unit","lead","cry","dark","us",
             "machine","note","wait","plan","figure","star","box","noun","field","rest","correct","able","pound","done","beauty","drive","stood","contain","front","teach","week","final","gave","green","oh","quick","develop",
             "sleep","warm","free","minute","strong","special","mind","behind","clear","tail","produce","fact","street","inch","lot","nothing","course","stay","wheel","full","force","blue","object","decide","surface","deep",
             "moon","island","foot","yet","busy","test","record","boat","common","gold","possible","plane","age","dry","wonder","laugh","thousand","ago","ran","check","game","shape","yes","hot","miss","brought","heat","snow",
             "bed","bring","sit","perhaps","fill","east","weight","language","among","nasa","harry","cipher","nuclear","war","catastrophe","apollo","one","two","three","four","five","six","seven","eight","nine","ten","eleven",
             "twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eightteen","nineteen","twenty","apollo","lunar","mission","phase","orbit","orbital","prime","objective","spacecraft","meg","file","luna","programme",
             "state","department","united","states","america","usa","uk","britain","americas","gene","conscience","plot","wisdom","neil","file","files","coincidence","once","twice","navigation","saturn"]
# COPY-PASTE for adding words to freqWords array: "",
# Add extra words to the array to get better accuracy when detecting english and generating key
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

#==============================================================================================================================================================
#                                                       TEXT MANIPULATION AND REPEATED USE FUNCTIONS - DO NOT EDIT
#==============================================================================================================================================================

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
'''
def clearScoreEnglish(cipherText): # clear Score function that returns % english when string inputted 
    def searchWords(cipherWord,freqWords):
        freqPosition = 0
        english = False
        while freqPosition < len(freqWords) and not english: # Linear searches a specific word with the english language
            if freqWords[freqPosition] == cipherWord:
                english = True
            freqPosition += 1
        return english
    cipherEnglishArray = []
    cipherTextSplit = cipherText.split()
    cipherPosition = 0
    while cipherPosition < len(cipherTextSplit):
        cipherEnglish = searchWords(cipherTextSplit[cipherPosition],freqWords) 
        cipherEnglishArray.append(cipherEnglish) # puts all the T's and F's into an array
        cipherPosition += 1
    trues = cipherEnglishArray.count(True)
    clearScore = round((trues / len(cipherEnglishArray)) * 100) # Calculates how many T's there are in array and outputs a % english
    cipherEnglishArray.clear()
    return clearScore
'''
def characterFrequency(encryptedTextUnformatted):
    encryptedText = removeSpaces(removePunctuation(encryptedTextUnformatted))
    frequencies = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in encryptedText: #iterates through each character in encrypted_cipher text
        index = 0 #element index set at 0
        #WHEN data at index (character in encrypted text) does not equal first element
        #AND the alphabet index is less than 25, (i.e all letters encompassed only):
        while i != letter[index] and index < 25: #THEN increment pos index ++, avoids indexing greater than alphabet list
           if index <= 24:
               index += 1
        else: #increments relative index dependant upon character contained within i
            if i == letter[index]:
                frequencies[index] = frequencies[index] + 1 #if character in encrypted_text is a space,data @ alphabet[26] ++:           
    return frequencies
def indexOfCoincidence(text): #String input to calculate the Index of Coincidence of a text
    def letter(letterCount,textLength):
        letterValue = (letterCount / textLength)*((letterCount - 1)/(textLength - 1))
        return letterValue
    IoCARRAY = []
    alphaIndex = 0
    textArray = convertToASCII(list(removeSpaces(removePunctuation(text))))
    textLength = len(textArray)
    while alphaIndex < 26:
        letterCount = textArray.count(alphaIndex + 97)
        IoCARRAYStore = (letter(letterCount,textLength))
        IoCARRAY.append(IoCARRAYStore)
        alphaIndex += 1
    IoC = sum(IoCARRAY)
    return IoC
def chiSquaredStat(text): #String input which calculates the chi-squared statistic of a text
    def letter(realLetterCount,expectedLetterCount):
        letterValue = ((realLetterCount - expectedLetterCount)**2) / expectedLetterCount
        return letterValue
    chiSquaredARRAY = []
    alphaIndex = 0
    textArray = convertToASCII(list(removeSpaces(removePunctuation(text))))
    textLength = len(textArray)
    while alphaIndex < 26: 
        realLetterCount = textArray.count(alphaIndex + 97)
        expectedLetterCount = textLength * englishLetterFrequencyProbability[alphaIndex] #Compares it against an english distribution
        chiSquaredARRAYStore = letter(realLetterCount,expectedLetterCount)
        chiSquaredARRAY.append(chiSquaredARRAYStore)
        alphaIndex += 1
    chiSquared = sum(chiSquaredARRAY)
    return chiSquared
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

#==============================================================================================================================================================
#                                                            CIPHER SOLVING - EDITABLE
#==============================================================================================================================================================

def ceaser(string, shift): # Ceaser shift function
    cipher = ""
    for char in string:
      if char == " ":
        cipher = cipher + char #leaves spaces
      else:
        cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97) #Shifts all lowercases
    return cipher
def randomKey(): #generates a random key
    perms = 0
    key = []
    while perms < 26: #Ensures 26 letters in the alphabet
        randomNo = random.randint(97, 122)
        repeat = search(randomNo,key) #Ensures each letter is unique
        if repeat == False:
            key.append(randomNo)
            perms += 1
    finalKey = "".join(convertToCHARACTER(key))
    return finalKey
def keyWordRandom(index): #Keyword key generator - filled in bit being random characters
    key = convertToASCII(list(freqWords[index]))
    countIndex = 0
    while countIndex < 26: #Removes duplicate letters any words may have
        howMany = key.count(alphabetASCII[countIndex])
        if howMany >= 2:
            where = key.index(alphabetASCII[countIndex])
            while howMany > 1:
                key.pop(where)
                where = key.index(alphabetASCII[countIndex])
                howMany -= 1
        countIndex += 1
    perms = len(key)
    while perms < 26: #Ensures 26 letters in the alphabet
        randomNo = random.randint(97, 122)
        repeat = search(randomNo,key) #Ensures each letter is unique
        if repeat == False:
            key.append(randomNo)
            perms += 1
    finalKey = "".join(convertToCHARACTER(key))
    return finalKey
def keyWordAlphabet(index): #Keyword key generator - filled in bit being the alphabet
    key = convertToASCII(list(freqWords[index]))
    countIndex = 0
    while countIndex < 26: #Removes duplicate letters any words may have
        howMany = key.count(alphabetASCII[countIndex])
        if howMany >= 2:
            where = key.index(alphabetASCII[countIndex])
            while howMany > 1:
                key.pop(where)
                where = key.index(alphabetASCII[countIndex])
                howMany -= 1
        countIndex += 1
    perms = 0
    repeat = False
    while perms < 26: #Ensures 26 letters in the alphabet
        newChar = alphabetASCII[perms]
        repeat = search(newChar,key) #Ensures each letter is unique
        if repeat == False:
            key.append(newChar)
        perms += 1
    finalKey = "".join(convertToCHARACTER(key))
    return finalKey

def searchFrequencyAnalysis(itemToCheckFor): #Compares the inputted value to standard english language letter freuqnecy and finds the closest value and returns its letter position (a=0 b=1 etc) [all in %]
    def searchFrequencyAnalysisSorted(positionToMap): #Takes both the sorted alphabet and normal alphabet and maps the positions from the ciphertext frequency analysis
        value = englishLetterFrequencySorted[positionToMap]
        mappedPosition = englishLetterFrequency.index(value)
        return mappedPosition
    position = 0
    betweenValues = positionSortedAlphabetZero = False
    while position < 26 and not betweenValues:
        if englishLetterFrequencySorted[position] > itemToCheckFor: #compares to the first, and because sorted, highest value and if it is less than it will move onto the second ( next highest)
            if position == 25: #If a value lower than the lowest value is inputted it will bypass everything else (ie input of 0 or less than 0.074)
                positionSortedAlphabetZero = True
            position += 1
        elif englishLetterFrequencySorted[position] < itemToCheckFor: #Does the above until it it greater than the next value so it must be between position and the previous position ( position - 1 )
            betweenValues = True
        if betweenValues == True: #its greater than the position but less than position - 1
            differenceAbove = round(englishLetterFrequencySorted[(position - 1)] - itemToCheckFor,10)
            differentBelow = round(itemToCheckFor - englishLetterFrequencySorted[position],10)
            if differenceAbove > differentBelow and positionSortedAlphabetZero == False: # if the upper different is bigger it is closer to position
                positionSortedAlphabet = position
            elif differenceAbove < differentBelow and positionSortedAlphabetZero == False: # if the lower different is bigger it is closer to position - 1
                if position != 0: 
                    positionSortedAlphabet = position - 1
                else: # if bigger than 12.702 and therefore first or 0th
                    positionSortedAlphabet = position
            positionIndexed = searchFrequencyAnalysisSorted(positionSortedAlphabet)#translates the indexing from the sorted alphabet into the normal alphabet
        elif positionSortedAlphabetZero == True: #Bypass for inputs less than 0.074
            positionSortedAlphabet = 25
            positionIndexed = searchFrequencyAnalysisSorted(positionSortedAlphabet)#translates the indexing from the sorted alphabet into the normal alphabet
    return positionIndexed


def frequencyKey(cipherTextToBeFREQQED): #Function to return the key with accordance to comparisons between the ciphertext frequency analysis and the frequency analysis of english plaintext
    #cipherTextToBeFREQQED is a user inputted string
    frequencyOfCipherText = characterFrequency(cipherTextToBeFREQQED) #gets the frequency analysis data of the string inputted
    cipherTextNoSpaces = removePunctuation(removeSpaces(cipherTextToBeFREQQED)) #removes spaces and punctuation of ciphertext
    cipherTextNoSpacesArray = list(cipherTextNoSpaces) #converts the formatted ciphertext into an array
    indexOfFrequencyAnalysis = 0
    while indexOfFrequencyAnalysis < 26: #Converts frequency analysis data from number of occurrences into a % of text frequency analysis
        frequencyOfCipherText[indexOfFrequencyAnalysis] = round(((frequencyOfCipherText[indexOfFrequencyAnalysis] / len(cipherTextNoSpacesArray))*100),3 )
        indexOfFrequencyAnalysis += 1
    indexToCompare = loopIteration = 0
    englishIndexOrderArray = []
    randomIncrease = 100
    lowerRandom = -2
    upperRandom = 2
    while indexToCompare < 26: 
        #Matches the frequencies of individual letters in the ciphertext to that of english producing a key
        #Gets the frequency of ciphertext in % and compares it to the % of english and then returns an array with the positions of the closest values
        englishIndex = searchFrequencyAnalysis(frequencyOfCipherText[indexToCompare])
        duplicates = False
        unCertainty = random.randint(lowerRandom,upperRandom) #Adds uncertainty to the letters so higher chance of finding a correct key (bigger numbers longer key generation time)
        randomisedEnglishIndex = englishIndex + unCertainty
        duplicates = search(randomisedEnglishIndex,englishIndexOrderArray) #Ensures no duplicates of positions
        if duplicates == False and randomisedEnglishIndex < 27 and randomisedEnglishIndex > 0:
            englishIndexOrderArray.append(randomisedEnglishIndex) #adds each letter mapped to the new letter position to this array (a=0 b=1 etc etc)
            indexToCompare = indexToCompare + 1 #Only increases if there is no duplicates and therefore something new got added else it will repeat until this does happen
        if loopIteration == randomIncrease: # to stop an endless cycle if it has looped 100 times without successfully finding a letter it increases the randomness until it eventually works
            lowerRandom += -1
            upperRandom += 1
            randomIncrease += 200
        loopIteration += 1
    convertASCIIIndex = 0 # Text formatting
    while convertASCIIIndex < 26: #converts the a=0 b=1 (positional data) to ASCII numbers
        englishIndexOrderArray[convertASCIIIndex] = englishIndexOrderArray[convertASCIIIndex] + 96
        convertASCIIIndex += 1
    finalKey = "".join(convertToCHARACTER(englishIndexOrderArray)) #converts the ASCII index to a plaintext string key with 26 characters
    return finalKey


'''
def iterativeSolving(userCipherText):
    parentKey = randomKey()#frequencyKey(userCipherText) #parent Key is generated using frequency analysis
    decipher = substitionKeyCipher(userCipherText,parentKey) #solves parent cipher using the parent key
    parentScore = ngramFitness(userCipherText,ngramDitionaryEnglish) #Gets the text fitness of this ciphertext
    iteration = 0
    while iteration < 1000:
        a = random.randint(0,25) #2 random letters (numbers) generated
        b = random.randint(0,25)
        childKeyArray = list(parentKey) #converts parent key string into a child array
        childKeyArray[a],childKeyArray[b] = childKeyArray[b],childKeyArray[a] # swap two characters in the child
        childKey = "".join(childKeyArray) #converts child key array into a string
        decipher = substitionKeyCipher(userCipherText,childKey) #deciphers the ciphertext with the new jumbled key
        childScore = ngramFitness(decipher,ngramDitionaryEnglish) #gets the text fitness score of the new ciphertext
        if childScore > parentScore: # if the child was better, replace the parent with it. Else dont...
            parentScore = childScore
            parentKey = childKey
            iteration = 0 #reset the iteration count to 0 as it is getting better and is not at a local minimum
        iteration += 1
        if childScore > -150:
            return childKey
    return childKey
'''
def iterativeSolving(cipherTextYY,maxScore):
    #cipherText  = re.sub("[^A-Z]","",cipherTextYY.upper())
    cipherText = removePunctuation(removeSpaces(cipherTextYY)).upper()
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
        maxScore = parentScore
        r = "".join(parentKey)
        t = r.lower()
        return t

#rbo rpktigo vcrb bwucja wj kloj hcjd km sktpqo cq rbwr loklgo vcgg cjqcqr kj skhcja wgkja wjd rpycja rk ltr rbcjaq cj cr

#==============================================================================================================================================================
#                                                   USER INPUT / OUTPUT                   MAIN PROGRAM
#==============================================================================================================================================================

userKey = "abcdefghijklmnopqrstuvwxyz" #Sets a defult user key ~~~~WARNING~~~~ Wont show error if there is not a key generated as this one will take over ~~~~WARNING~~~~
keyIterations = keyWordAlphabetIndex = keyWordRandomIndex = frequencyKeyIndex = randomKeyIndex = ceaserShifts = iterativeSolvingIndex = REPLACEME123 = 0
maxScoreIterative = -99e9
#Turn each function on or off
keyWordAlphabetStart = False
keyWordRandomStart = False
frequencyKeyStart = False
randomKeyStart = False
ceaserStart = False
iterativeSolvingStart = True

while True == True: #Loops the entire program
    userCipher = removeSpaces(removePunctuation((input(cipherSolverInputFormat)).lower()))
    #########################################################
    #           Calling different deciphering functions
    #########################################################
    while keyIterations < keyIterations + 1:
        if ceaserStart == True: #Ceaser shifts done 26 times
            userKey = ceaser("abcdefghijklmnopqrstuvwxyz", 26 - ceaserShifts)
            cipherOut = ceaser(userCipher, ceaserShifts)
            ceaserShifts += 1
        elif keyWordAlphabetStart == True: # Keyword keys done for all key words with the last letters being random
            userKey = keyWordAlphabet(keyWordAlphabetIndex)
            cipherOut = substitionKeyCipher(userCipher,userKey)
            keyWordAlphabetIndex += 1
        elif keyWordRandomStart == True: # Keyword keys done for all key words with the last letters being the alphabet
            userKey = keyWordRandom(keyWordRandomIndex)
            cipherOut = substitionKeyCipher(userCipher,userKey)
            keyWordRandomIndex += 1
        elif frequencyKeyStart == True: #Key generated from advanced frequency analysis
            userKey = frequencyKey(userCipher)
            cipherOut = substitionKeyCipher(userCipher,userKey)
            frequencyKeyIndex += 1
        elif randomKeyStart == True: # Last resort random keys
            userKey = randomKey()
            cipherOut = substitionKeyCipher(userCipher,userKey)
            randomKeyIndex += 1
        elif iterativeSolvingStart == True: # Last resort random keys
            userKey = iterativeSolving(userCipher,maxScoreIterative)
            cipherOut = substitionKeyCipher(userCipher,userKey)
            iterativeSolvingIndex += 1
        #########################################################
        #                   Text statistics
        #########################################################
        #clearScore = clearScoreEnglish(cipherOut) 
        indexOfCoincidenceText = round(indexOfCoincidence(cipherOut),10)
        chiSquaredText = round(chiSquaredStat(cipherOut),10)
        ngramScore = ngramFitness(cipherOut,ngramDitionaryEnglish)
        cipherOutKeyOut ='''
================== PLAINTEXT: ==================
{printedCipherOut}
===================== KEY: =====================
{printedUserKey}
================= STATISTICS: ==================
Number of keys          {printedAttempts}
log Ngram Score         {printedNgramScore}
Index Of Coincidence    {printedIoC}
Chi Squared             {printedChi}
'''.format( #English Score           {printedClearScore}%
        printedCipherOut = cipherOut, 
        printedUserKey = userKey,
        #printedClearScore = clearScore,
        printedNgramScore = ngramScore,
        printedAttempts = keyIterations, 
        printedIoC = indexOfCoincidenceText, 
        printedChi = chiSquaredText )#Formatting
        if ngramScore > -300:
            print(cipherOutKeyOut)
        keyIterations += 1


######  TEST CIPHERS TO TRY AND SOLVE  ######
#rbo rpktigo vcrb bwucja wj kloj hcjd km sktpqo cq rbwr loklgo vcgg cjqcqr kj skhcja wgkja wjd rpycja rk ltr rbcjaq cj cr
#Tjf, B sppx r ippx rs sqj ubij vpd hjes pojw rey bs zrh mdhs r wpsrsbpe nbaqjw raaibjy sp sqj sjks. Rs ubwhs bs zrh qrwy sp hrv bu sqrs zrh r cdf pw r ujrsdwj rey epwtriiv B zpdiy rhhdtj cdf, cds bs hjjtjy pyy sqrs bs zrh sqj peiv ubij sqrs zrh ruujnsjy hp B rhxjy rwpdey sp hjj bu revpej qry hjje revsqbef hbtbirw. Bs sdweh pds sqrs sqbh zrh eps sqj ubwhs erobfrsbpe awpcijt sp qbs sqj awpfwrttj. Fjej wjapwsjy r trmpw bhhdj zbsq sqj fdbyrenj awpfwrttj upw Heppav pe sqj Rapiip Sje tbhhbpe zqbnq npdiy rfrbe qroj nrdhjy r trmpw awpcijt. Upw hptj wjrhpe sqj awpfwrttj npeswpiibef sqj ireybef wryrw zrhe’s dayrsjy zbsq sqj uibfqs aire rey bu Fjej qrye’s wrbhjy sqrs zbsq Bojwhpe sqje sqj cpvh tbfqs qroj qry wjri swpdcij fjssbef crnx. B ippxjy sqwpdfq sqj nptarev ubijh rey updey repsqjw pu pdw tvhsjwbpdhiv upwtrssjy wjapwsh: sqj tjtp beupwtbef sqjt rcpds sqj nqrefj, zqbnq jkairbeh zqv sqj awpfwrttj ejojw fps dayrsjy. Sqbh sbtj sqj nbaqjw zrh re ruubej hqbus, hp hibfqsiv qrwyjw sp nwrnx, cds epsqbef hjwbpdh. Hsbii, bs bh tdnq ijhh ibxjiv sqrs bs zrh r cdf sqrs sbtj, rey be rev nrhj szbnj bh spp tdnq pu r npbenbyjenj. Bs yby hsrws tj zpeyjwbef zqv sqj hjnpey nbaqjw zrh jrhbjw sp nwrnx sqre sqj ubwhs, cds sqje B wjribhjy sqrs sqj ruubej hqbus zrh spp tdnq pu r fbojrzrv. R wpsrsbpe nbaqjw wjriiv npdiy mdhs cj re jenpybef jwwpw, cds sqj ruubej hqbus bh spp hpaqbhsbnrsjy upw r tbhsrxj, hp zqpjojw trefijy sqj wjapwsh tdhs qroj wjribhjy sqjv qry tryj r cbs pu re jwwpw zbsq sqj ubwhs pej rey swbjy sp npojw sqjbw hsjah zbsq sqj hjnpey. Bs bh qrwy sp hjj sqbh rh revsqbef psqjw sqre rssjtasjy hrcpsrfj, cds B rt eps hdwj zqrs sqj tpsboj npdiy cj. B ypdcs bs bh ajwhperi. Sqj Rapiip Sje rey Jijoje nwjzh ype’s pojwira, hp jbsqjw hptjpej qrh r fwdyfj rfrbehs sqj zqpij Rhswperds npwah pw sqjv rwj swvbef sp yjwrbi sqj Rapiip awpfwrttj. Bs npdiy cj sqj Hpobjsh B hdaaphj. Rs ubwhs, B sqpdfqs sqrs sqjbw zbiibefejhh sp hqbus sqj IDER-UBUSJJE pwcbs hqpzjy sqrs sqjv zjwje’s arws pu bs, cds hptjpej be sqj Hsrsj Yjarwstjes apbesjy pds sqrs sqjv tbfqs mdhs qroj qry r fdbisv npehnbjenj, pw cjje xjje sp ybhsrenj sqjthjiojh penj sqj aips zrh ybhnpojwjy. B rt hsbii eps hdwj. Be sqj tjresbtj, npdiy vpd srxj r ippx rs sqj nptadsjw ubijh sp hjj zqp tbfqs qroj qry rnnjhh sp cpsq tjtph, rey zqp tbfqs qroj qry sqj paapwsdebsv rey tjreh sp ypnspw sqjt? B rt uivbef crnx sp Irefijv spebfqs, sp hjj bu sqj Hsrsj Yjarwstjes qroj rev byjrh zqrs tbfqs cj fpbef pe. Ejbi hrby qj npdiy uiv tj da be pej pu sqj ERHR nqrhj airejh, zqbnq bh hptjsqbef B qroj cjje xjje sp swv. B zbii nrii vpd bu B fjs revsqbef.
#xqhho y qc dej ikhu yv oek muhu sefyut yd je jxu cuce qrekj husudj uludji rkj xuhu yi q ikccqho jme tqoi qwe qd evvtkjo wkytqdsu evvysuh qbuhjut cyiiyed sedjheb je q fejudjyqb fherbuc myjx jxu qfebbe vbywxj jxu fbqddut tuisudj jhqzusjeho qffuqhut je ru hkddydw ed q sebbyiyed sekhiu myjx

#WKMPC ZKXDV SYEZU KYLTV ICYFK BVDDN KZKXD VMYXO BPKLP XMDNK CDVLL VXTDB IPXMD YMVEM KDNKW YYTDN KBKIY EVBKB PMNDD NKNVG RCVBK MKDDP XMZBK DDIBK CDUKC CVXTN VFKWY BKYBU KCCTK SPTKT VUBKV TIDNV DDNKC YFPKD CVBKD YOUVW KLYBB KSKXD KFKXD CYXDN KVZYU UYZBY MBVWW KCYWK YLDNK MKXKB VUCTY XDXKK TWESN YLVXK HSECK DYDEB XEZDN KNKVD OEDIY ETYXD MKDLY EBCDV BCGPD NYEDE XTKBC DVXTP XMDNK XKKTL YBZYU PDPSV UCEZZ YBDVX TDNKB KNVCO KKXVS YXSKB DKTGN PCZKB PXMSV WZVPM XDYSY XFPXS KDNKZ BKCPT KXDDY DVRKV CDBYX MUPXK DNKWY CDCDB PTKXD VBKSV UUPXM LYBVU VBMKO EPUTE ZYLLY BSKCV UYXMD NKOYB TKBGP DNKVC DMKBW VXIVC VCNYG YLCDB KXMDN VBMEP XMDNV DDNKV DDVSR YXDNK CZVSK ZBYMB VWWKW ECDNV FKOKK XVEDN YBPCK TOIDN KZYUP DOEBY DNVDW VRKCX YCKXC KDYWK LPBCD DNKBE CCPVX CVBKW YBKUP RKUID YDBID YGPXD NKZBY ZVMVX TVGVB DNVXD YBPCR SYXLU PSDVX TCKSY XTDNK CVOYD VMKPL DNVDP CGNVD PDPCP CXDCY ZNPCD PSVDK TKXYE MNLYB VRMOY ZKBVD PYXOE DPDPC NVBTD YSYXF PXSKD NKMKX KBVUC DNVDD NVDPC DBEKC YWKYL DNKWY BKSVE DPYEC ZUVXX KBCWY CDUID NYCKG NYVSD EVUUI LYEMN DPXDN KUVCD GVBNV FKWVX VMKTD YOUYS RDNKO EPUTE ZZBYZ YCPXM VXKGD BVXSN KYLGV BMVWK CPXCD KVTWY OPUPC PXMDN VDGVI PCCDP UUVZB YFYSV DPYXO EDPCU KCCUP RKUID YVSSP TKXDV UUIDB PMMKB VGVBK CZKSP VUUIP LGKXY DPLIZ VFUYF CRIPX VTFVX SKVUU DNKCV WKWIY GXDPW KPXOK BUPXS YXFPX SKTWK GKNVF KDYDB KVTFK BICYL DUIDN KBKCY PNKVT KTYFK BDYUV XMUKI VXTSY XFPXS KTDNK WDYCE MMKCD VXVUD KBXVD PFKGK GPUUC DKZEZ PXCZK SDPYX CVDSN KSRZY PXDSN VBUPK DYWVR KPDNV BTKBL YBCYF PKDVM KXDCD YSBYC CVXTS BVXRE ZDNKD KELKU COKBM UPCDK XPXMY ZKBVD PYXDY CKKPL DNVDD EBXCE ZVXID NPXMB KUVDK TPVWV UCYMY PXMDY CKXTV SYEZU KYLYE BOKCD YFKBD YOVPR YXEBD YDBIV XTLPX TYEDG NVDPC MYPXM YXDNK BKDNK CYFPK DCVBK ZBKDD ICKSB KDPFK VOYED DNKPB YGXCZ VSKZB YMBVW WKVXT GPDNY EDDNK GYBUT CZBKC CGVDS NPXMG KTYXD BKVUU INVFK VSUKV BZPSD EBKYL DNKPB ZBYMB KCCYB DNKPB ZUVXC EXUKC CDNKI VBKSU YCKDY ZEDDP XMDNK PBYGX WKXYX DNKWY YXPSV XDCKK GNVDD NKINV FKDYM VPXGP DNGNV DCKKW CDYOK VLVPB UITPC YBMVX PCKTV DDKWZ DDYTK BVPUY EBCZV SKZBY MBVWW KOEDP GYEUT CDPUU UPRKD YRXYG GNVDD NKIVB KEZDY RKKZV SUYCK KIKYX DNKWP CCPYX ZUVXX PXMVX TUKDW KRXYG PLIYE NKVBV XIDNP XMGYB BIPXM PGPUU OKOVS RVOYE DVGKK ROKLY BKDNK UVEXS NNVBB I

# Find some typical log probabilities for english texts and for texts with different ciphers put through them to get a rough guage of how fit it is



#out  = re.sub("[^A-Z]","",string)
#WORK ON EFFICIENCY OF FILES TODO:
#make the quadgram file readlines
#make everything transmit data with lowercase strings
#make remove spaces and remove punctuation more efficient using re.
#remove clearscore
#make freqwords a txt file which can be used for keywords
#make ngram fitness more efficent
#improve general efficieny
#add functions to different files then import them into main program