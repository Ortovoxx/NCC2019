#==============================================================================================================================================================
#                                                                  VARIABLES, CONSTANTS AND FORMATTING - DO NOT EDIT
#==============================================================================================================================================================

import random
import time

cipherSolverInputFormat = '''*************** CIPHERTEXT: **************
'''
textManipulationInputFormat = '''*********** INPUT YOUR TEXT: ***********
'''
alphabetASCII = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
alphabetCHARACTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#IN %
englishLetterFrequency = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]
englishLetterFrequencySorted = [12.702,9.056,8.167,7.507,6.966,6.749,6.327,6.094,5.987,4.253,4.025,2.782,2.758,2.406,2.360,2.228,2.015,1.974,1.929,1.492,0.978,0.772,0.153,0.150,0.095,0.074]
#Probabilty /1
englishLetterFrequencyProbability = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]
# the above array numbers map to the following letters (in order)           e t a o i n s h r d l c u m w f g y p b v k j x q z
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
# Add extra words to the array to get better accuracy when detecting english

#==============================================================================================================================================================
#                                                       TEXT MANIPULATION AND REPEATED USE FUNCTIONS - DO NOT EDIT
#==============================================================================================================================================================

def convertToASCII(text): #Converts an array of characters into an array of their ASCII equivalent numbers
    perm = 0
    while perm < len(text): #goes through each array index and turns it from Character to ASCII
        text[perm] = ord(text[perm])
        perm = perm + 1
    return text
def convertToCHARACTER(text): #Converts an array of ASCII equivalent numbers into an array of their ASCII equivalent characters
    perm = 0
    while perm < len(text): #goes through each array index and turns it from ASCII number to Character
        text[perm] = chr(text[perm])
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
def reverseString(string): #Reverses the text
    return string[::-1]
def search(itemToCheckFor,listToSearchFrom): #LINEAR SEARCH GLOBAL FUNCTION - Searches to see if there are repeats for random and keyword keys
    position = 0
    found = False
    while position < len(listToSearchFrom) and not found:
        if listToSearchFrom[position] == itemToCheckFor:
            found = True
        position = position + 1
    return found
def substitionKeyCipher(userCipherText,userKey): #maps a ciphertext to plaintext according to the key given to it
    cipherText = convertToASCII(list(userCipherText)) #Converting cipher to numbers
    key = convertToASCII(list(userKey)) #Converting key to numbers
    def switchChar(cipherChar): #Switches a single character from its chiphertext to its plaintext
        alphaPerm = 0
        newChar = 0
        while alphaPerm < len(alphabetASCII): #as it goes through a letter it changes it 
            if cipherChar == key[alphaPerm]:
                newChar = alphabetASCII[alphaPerm]
            alphaPerm = alphaPerm + 1
        return newChar
    textPerm = 0
    switchedCipher = []
    while textPerm < len(cipherText): #Goes through each character one by one and sends to the function which converts cipher to plain
        switchedCipher.append(switchChar(cipherText[textPerm]))
        textPerm = textPerm + 1
    switchedCipherStr = "".join(convertToCHARACTER(switchedCipher))
    return switchedCipherStr
def clearScoreEnglish(cipherText): # clear Score function that returns % english when string inputted #BUG I THINK IT DOESNT WORK IF THERE ARE SPACES -FIXME
    def searchWords(cipherWord,freqWords):
        freqPosition = 0
        english = False
        while freqPosition < len(freqWords) and not english: # Linear searches a specific word with the english language
            if freqWords[freqPosition] == cipherWord:
                english = True
            freqPosition = freqPosition + 1
        return english
    cipherEnglishArray = []
    cipherTextSplit = cipherText.split()
    cipherPosition = 0
    while cipherPosition < len(cipherTextSplit):
        cipherEnglish = searchWords(cipherTextSplit[cipherPosition],freqWords) 
        cipherEnglishArray.append(cipherEnglish) # puts all the T's and F's into an array
        cipherPosition = cipherPosition + 1
    trues = cipherEnglishArray.count(True)
    clearScore = round((trues / len(cipherEnglishArray)) * 100) # Calculates how many T's there are in array and outputs a % english
    cipherEnglishArray.clear()
    return clearScore
def characterFrequency(encryptedText):
    frequencies=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    for i in encryptedText: #iterates through each character in encrypted_cipher text
        index = 0 #element index set at 0
        #WHEN data at index (character in encrypted text) does not equal first element
        #AND the alphabet index is less than 25, (i.e all letters encompassed only):
        while i != letter[index] and index < 25: #THEN increment pos index ++, avoids indexing greater than alphabet list
           if index <= 24:
               index = index + 1
        else: #increments relative index dependant upon character contained within i
            if i == letter[index]:
                frequencies[index] = frequencies[index]+1 #if character in encrypted_text is a space,data @ alphabet[26] ++:
            elif i == " ":
                 frequencies[26]= frequencies[26]+1 #if character in encrypted_text therefore is not a recognised characer,data @ alphabet[27] ++
            else:
                frequencies[27]= frequencies[27]+1              
    return frequencies
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


#==============================================================================================================================================================
#                                                            CIPHER SOLVING - EDITABLE
#==============================================================================================================================================================


# TODO
#NO DUPLICATION KEYS
#KEY STORAGE - high intensity

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
    while perms < len(alphabetASCII): #Ensures 26 letters in the alphabet
        randomNo = random.randint(97, 122)
        repeat = search(randomNo,key) #Ensures each letter is unique
        if repeat == False:
            key.append(randomNo)
            perms = perms + 1
    finalKey = "".join(convertToCHARACTER(key))
    return finalKey
def keyWordRandom(index): #Keyword key generator - filled in bit being random characters
    key = convertToASCII(list(freqWords[index]))
    countIndex = 0
    while countIndex < len(alphabetASCII): #Removes duplicate letters any words may have
        howMany = key.count(alphabetASCII[countIndex])
        if howMany >= 2:
            where = key.index(alphabetASCII[countIndex])
            while howMany > 1:
                key.pop(where)
                where = key.index(alphabetASCII[countIndex])
                howMany = howMany - 1
        countIndex = countIndex + 1
    perms = len(key)
    while perms < len(alphabetASCII): #Ensures 26 letters in the alphabet
        randomNo = random.randint(97, 122)
        repeat = search(randomNo,key) #Ensures each letter is unique
        if repeat == False:
            key.append(randomNo)
            perms = perms + 1
    finalKey = "".join(convertToCHARACTER(key))
    return finalKey
def keyWordAlphabet(index): #Keyword key generator - filled in bit being the alphabet
    key = convertToASCII(list(freqWords[index]))
    countIndex = 0
    while countIndex < len(alphabetASCII): #Removes duplicate letters any words may have
        howMany = key.count(alphabetASCII[countIndex])
        if howMany >= 2:
            where = key.index(alphabetASCII[countIndex])
            while howMany > 1:
                key.pop(where)
                where = key.index(alphabetASCII[countIndex])
                howMany = howMany - 1
        countIndex = countIndex + 1
    perms = 0
    repeat = False
    while perms < len(alphabetASCII): #Ensures 26 letters in the alphabet
        newChar = alphabetASCII[perms]
        repeat = search(newChar,key) #Ensures each letter is unique
        if repeat == False:
            key.append(newChar)
        perms = perms + 1
    finalKey = "".join(convertToCHARACTER(key))
    return finalKey


#BUG - RETURNS 5 ALL OF FREQUENCYKEY IS WORKING FINE BUT THIS ALWAYS RETURNS 0 OR 5
def searchFrequencyAnalysis(itemToCheckFor,listToSearchFrom): #searches for the closest value to the ones inputted to the ones in english letter frequency
    def searchFrequencyAnalysisSorted(positionToMap,frequencySorted,frequency): #Takes both the sorted alphabet and normal alphabet and maps the positions from the ciphertext frequency analysis
        index = 0
        indexSorted = 0
        found = False
        while indexSorted < len(frequencySorted) and not found:
            while index < len(frequency) and not found:
                if frequencySorted[indexSorted] == frequency[index]:
                    found = True
                index = index + 1
            indexSorted = indexSorted + 1
        return index
    #######
    position = 0
    betweenValues = False
    positionIndexed = 0
    while position < len(listToSearchFrom) and not betweenValues:
        if listToSearchFrom[position] > itemToCheckFor: #compares to the first, and because sorted, highest value and if it is less than it will move onto the second ( next highest)
            position = position + 1
        elif listToSearchFrom[position] < itemToCheckFor: #Does the above until it it greater than the next value so it must be between position and the previous position ( position - 1 )
            betweenValues = True
        if betweenValues == True: #its greater than the position but less than position - 1
            differenceAbove = listToSearchFrom[(position - 1)] - itemToCheckFor
            differentBelow = itemToCheckFor - listToSearchFrom[position]
            if differenceAbove > differentBelow: # if the upper different is bigger it is closer to position
                positionSortedAlphabet = position
            else: #elif differenceAbove < differentBelow # if the lower different is bigger it is closer to position - 1
                positionSortedAlphabet = position - 1
            positionIndexed = searchFrequencyAnalysisSorted(positionSortedAlphabet,englishLetterFrequencySorted,englishLetterFrequency)#translates the indexing from the sorted alphabet into the normal alphabet
    return positionIndexed

#test cipher
#xqhho y qc dej ikhu yv oek muhu sefyut yd je jxu cuce qrekj husudj uludji rkj xuhu yi q ikccqho jme tqoi qwe qd evvtkjo wkytqdsu evvysuh qbuhjut cyiiyed sedjheb je q fejudjyqb fherbuc myjx jxu qfebbe vbywxj jxu fbqddut tuisudj jhqzusjeho qffuqhut je ru hkddydw ed q sebbyiyed sekhiu myjx 

def frequencyKey(cipherTextToBeFREQQED): #Function to return the key with accordance to comparisons between the ciphertext frequency analysis and the frequency analysis of english plaintext
    #cipherTextToBeFREQQED is a string
    frequencyOfCipherText = characterFrequency(cipherTextToBeFREQQED) #gets the frequency analysis of the string inputted
    cipherTextNoSpaces = removePunctuation(removeSpaces(cipherTextToBeFREQQED)) #removes spaces and punctuation of ciphertext
    cipherTextNoSpacesArray = list(cipherTextNoSpaces) #converts ciphertext into an array
    indexOfFrequencyAnalysis = 0
    while indexOfFrequencyAnalysis < len(frequencyOfCipherText): #Turns it from how many occurrences into a % frequency analysis
        frequencyOfCipherText[indexOfFrequencyAnalysis] = round(((frequencyOfCipherText[indexOfFrequencyAnalysis] / len(cipherTextNoSpacesArray))*100),3 )
        indexOfFrequencyAnalysis = indexOfFrequencyAnalysis + 1
    indexToCompare = 0
    englishIndexOrderArray = []
    while indexToCompare < len(frequencyOfCipherText): 
        englishIndex = searchFrequencyAnalysis(frequencyOfCipherText[indexToCompare],englishLetterFrequencySorted) #Gets the frequency of ciphertext in % and compares it to the % of english and then returns an array with the positions
        unCertainty = random.randint(-5,5) #Adds uncertainty to the letters so higher chance of finding a match
        randomisedEnglishIndex = englishIndex + unCertainty
        duplicates = search(randomisedEnglishIndex,englishIndexOrderArray)
        while duplicates == True:
            unCertainty = random.randint(-5,5) #Adds uncertainty to the letters so higher chance of finding a match
            randomisedEnglishIndex = englishIndex + unCertainty
            duplicates = search(randomisedEnglishIndex,englishIndexOrderArray) #Ensures each letter in the array is 100% unique
        else: #elif duplicates == False
            englishIndexOrderArray.append(randomisedEnglishIndex) #adds each letter mapped to the new letter position to this array (a=0 b=1 etc etc)
        indexToCompare = indexToCompare + 1
    convertASCIIIndex = 0
    while convertASCIIIndex < len(englishIndexOrderArray): #converts the a=0 b=1 to ASCII 
        englishIndexOrderArray[convertASCIIIndex] = englishIndexOrderArray[convertASCIIIndex] + 97
        convertASCIIIndex = convertASCIIIndex + 1
    finalKey = "".join(convertToCHARACTER(englishIndexOrderArray)) #converts the ASCII index to a plaintext string key with 26 characters
    return finalKey
#==============================================================================================================================================================
#                                                   USER INPUT / OUTPUT                   MAIN PROGRAM
#==============================================================================================================================================================

while True == True: #Loops the entire program
    userKey = "abcdefghijklmnopqrstuvwxyz" #Sets a defult user key ~~~~WARNING~~~~ Wont show error if there is not a key generated as this one will take over ~~~~WARNING~~~~
    keyIterations = keyWordAlphabetIndex = keyWordRandomIndex = frequencyKeyIndex = randomKeyIndex = ceaserShifts = REPLACEME123 = 0
    #Turn each function on or off
    keyWordAlphabetStart = False
    keyWordRandomStart = False
    frequencyKeyStart = False
    randomKeyStart = True
    ceaserStart = False
    userCipher = input(cipherSolverInputFormat)
    ############################################
    while keyIterations < keyIterations + 1:
        if ceaserStart == True: #Ceaser shifts done 26 times
            userKey = ceaser("abcdefghijklmnopqrstuvwxyz", 26 - ceaserShifts)
            cipherOut = ceaser(userCipher, ceaserShifts)
            ceaserShifts = ceaserShifts + 1
        elif keyWordAlphabetStart == True: # Keyword keys done for all key words with the last letters being random
            userKey = keyWordAlphabet(keyWordAlphabetIndex)
            cipherOut = substitionKeyCipher(userCipher,userKey)
            keyWordAlphabetIndex = keyWordAlphabetIndex + 1
        elif keyWordRandomStart == True: # Keyword keys done for all key words with the last letters being the alphabet
            userKey = keyWordRandom(keyWordRandomIndex)
            cipherOut = substitionKeyCipher(userCipher,userKey)
            keyWordRandomIndex = keyWordRandomIndex + 1
        elif frequencyKeyStart == True: #Key generated from advanced frequency analysis
            userKey = frequencyKey(userCipher)
            cipherOut = substitionKeyCipher(userCipher,userKey)
            frequencyKeyIndex = frequencyKeyIndex + 1
        elif randomKeyStart == True: # Last resort random keys
            userKey = randomKey()
            cipherOut = substitionKeyCipher(userCipher,userKey)
            randomKeyIndex = randomKeyIndex + 1
        clearScore = clearScoreEnglish(cipherOut) #rbo rpktigo vcrb bwucja wj kloj hcjd km sktpqo cq rbwr loklgo vcgg cjqcqr kj skhcja wgkja wjd rpycja rk ltr rbcjaq cj cr
        indexOfCoincidenceText = round(indexOfCoincidence(cipherOut),10)
        chiSquaredText = round(chiSquaredStat(cipherOut),10)
        cipherOutKeyOut ='''
================== PLAINTEXT: ==================
{printedCipherOut}
===================== KEY: =====================
{printedUserKey}
================= STATISTICS: ==================
Number of keys          {printedAttempts}
English Score           {printedClearScore}%
Index Of Coincidence    {printedIoC}
Chi Squared             {printedChi}
'''.format(printedCipherOut = cipherOut, 
        printedUserKey = userKey,
        printedClearScore = clearScore, 
        printedAttempts = keyIterations, 
        printedIoC = indexOfCoincidenceText, 
        printedChi = chiSquaredText )#Formatting
        if clearScore > 1 and chiSquaredText < 300:
            print(cipherOutKeyOut)
        keyIterations = keyIterations + 1