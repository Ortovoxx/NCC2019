#==============================================================================================================================================================
#                                                                  VARIABLES, CONSTANTS AND FORMATTING - DO NOT EDIT
#==============================================================================================================================================================

import random
import time
mainMenuFormat = '''----------------------------------------
 1  -  Substition Cipher sovler
 2  -  Text Manipulator
----------- PROGRAM SELECT: ------------
'''
textManipulationMenuFormat = '''----------------------------------------

 1  -  Convert to lowercase
 2  -  Convert to uppercase
 3  -  Remove punctuation
 4  -  Reverse text
 5  -  Remove spaces
 6  -  Statistics
 7  -  Frequency analysis
 8  -  Advanced frequency analysis
 
---------------- SELECT: ---------------
'''
cipherSolverInputFormat = '''*************** CIPHERTEXT: **************
'''
textManipulationInputFormat = '''*********** INPUT YOUR TEXT: ***********
'''
freqWords = ["the","of","to","and","a","in","is","it","you","that","he","was","for","on","are","with","as","I","his","they","be","at","one","have","this","from","or","had","by","hot","but","some","what","there","we","can",
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
             "state","deparment","united","states","america","usa","uk","britain","americas","gene","conscience","plot","navigation","niel","file","files","coincidence","once","twice","wisdom",]
# COPY-PASTE for adding words to freqWords array: "",
# Add extra words to the array to get better accuracy when detecting english
alphabetASCII = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
alphabetCHARACTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#==============================================================================================================================================================
#                                                       TEXT MANIPULATION AND REPEATED USE FUNCTIONS - DO NOT EDIT
#==============================================================================================================================================================

def convertToASCII(text): #Converts an array of characters into an array of their ASCII equivilant numbers
    perm = 0
    while perm < len(text): #goes through each array index and turns it from Character to ASCII
        text[perm] = ord(text[perm])
        perm = perm + 1
    return text
def convertToCHARACTER(text): #Converts an array of ASCII equivilant numbers into an array of their ASCII equivilant characters
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
def clearScoreEnglish(cipherText): # clear Score function that returns % english when string inputted 
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
def search(itemToCheckFor,listToSearchFrom): #Searches to see if there are repeats for random and keyword keys
    position = 0
    found = False
    while position < len(listToSearchFrom) and not found:
        if listToSearchFrom[position] == itemToCheckFor:
            found = True
        position = position + 1
    return found

#==============================================================================================================================================================
#                                                            CIPHER SOLVING - EDITABLE
#==============================================================================================================================================================

#ADD TO THE KEY GENERTAION FUNCTION
#WORD KEYS
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

def keyGeneration(): #generates a random key
    key = []
    def randomKey(): #generates a random key
        perms = 0
        while perms < len(alphabetASCII): #Ensures 26 letters in the alphabet
            randomNo = random.randint(97, 122)
            repeat = search(randomNo,key) #Ensures each letter is unique
            if repeat == False:
                key.append(randomNo)
                perms = perms + 1
    #all the functions to call in order of importance
    randomKey()
    finalKey = "".join(convertToCHARACTER(key))
    return finalKey


def keyWord(): #Keyword key generator - INCOMPLETE
    perms = 0
    while perms < len(freqWords):
        keyWordASCII = convertToASCII(freqWords[perm])
        perms = perms + 1
    return finalKey

#==============================================================================================================================================================
#                                                   USER INPUT / OUTPUT                   MAIN PROGRAM
#==============================================================================================================================================================

#All the different statistic variables
characterCount = 1
symbolCount = 1
upperCount = 1
lowerCount = 1
numberCount = 1
spaceCount = 1
wordCount = 1
stats = '''========================================
 Statistics about inputted text:
 ========================================
 
   Characters:     {printedCharacterCount}
   Symbols:        {printedSymbolCount}
   Uppercases:     {printedUpperCount}
   LowerCases:     {printedLowerCount}
   Numbers:        {printedNumberCount}
   Spaces:         {printedSpaceCount}
   Words:          {printedWordCount}
 
 ========================================'''.format(
printedCharacterCount = characterCount,
printedSymbolCount = symbolCount,
printedUpperCount = upperCount,
printedLowerCount = lowerCount,
printedNumberCount = numberCount,
printedSpaceCount = spaceCount,
printedWordCount = wordCount) #Formatting

unixTimeFUNC = lambda: int(round(time.time() * 1000))# Unix time function work in progress
startUnix = unixTimeFUNC()
def unixTime():
    nowUnix = int(round(time.time() * 1000))
    endUnix = nowUnix - startUnix
    return endUnix



    
userKey = "abcdefghijklmnopqrstuvwxyz"
ceaserShifts = 0
while True == True: #Loops the entire program
    mainMenu = int(input(mainMenuFormat))
    while mainMenu == 1:
        #---------------------------------------------------------------------------------------------------------------
        #                                        CIPHER SOLVER MAIN PROGRAM
        #---------------------------------------------------------------------------------------------------------------
        keyIterations = 0
        keyCountPerSecond = 0
        keysPerSecond = 0
        randomKeyStart = True #Flag used to start the random key generation
        userCipher = input(cipherSolverInputFormat)
        while keyIterations < keyIterations + 1:
            if keyIterations < 26: #Ceaser shifts done 26 times
                userKey = ceaser("abcdefghijklmnopqrstuvwxyz", 26 - ceaserShifts)
                cipherOut = ceaser(userCipher, ceaserShifts)
                ceaserShifts = ceaserShifts + 1
#           elif keyIterations > 26 and keyIterations < len(freqWords): #Keyword keys done for all key words
#               userKey = keyWord()
#               cipherOut = substitionKeyCipher(userCipher,userKey)
#           elif n > len(freqWords) and randomKeyStart == False: #Key generated from advanced frequency analysis
#               userKey = frequencyKey()
#               cipherOut = substitionKeyCipher(userCipher,userKey)
            elif randomKeyStart == True: # Last resort random keys
                userKey = keyGeneration()
                cipherOut = substitionKeyCipher(userCipher,userKey)
            clearScore = clearScoreEnglish(cipherOut)
            cipherOutKeyOut ='''
=============== PLAINTEXT: ===============
{printedCipherOut}
================== KEY: ==================
{printedUserKey}
============== STATISTICS: ===============
Keys/s              {printedStatistics}
Number of attemps   {printedAttempts}
English Score       {printedClearScore}%
'''.format(printedCipherOut = cipherOut, printedUserKey = userKey, printedStatistics = keysPerSecond, printedClearScore = clearScore, printedAttempts = keyIterations)#Formatting
            if  clearScore> 10:
                print(cipherOutKeyOut)
            keyIterations = keyIterations + 1
            keyCountPerSecond = keyCountPerSecond + 1
    while mainMenu == 2:
        #---------------------------------------------------------------------------------------------------------------
        #                                             TEXT MANIPULATION MAIN PROGRAM
        #---------------------------------------------------------------------------------------------------------------
        plainText = input(textManipulationInputFormat)
        if plainText == "": # if enter is pressed the previous input will be carried forward
            if menu == 1:
                plainText = lowerCase
            elif menu == 2:
                plainText = upperCase
            elif menu == 3:
                plainText = noSymbol
            elif menu == 4:
                plainText = reversal
            elif menu == 5:
                plainText = noSpaces
        menu = int(input(textManipulationMenuFormat))
        if menu == 1: # MENU to select which function to use
            lowerCase = plainText.lower()
            print("\n", lowerCase, "\n")
        elif menu == 2:
            upperCase = plainText.upper()
            print("\n",upperCase, "\n")
        elif menu == 3:
            noSymbol = removePunctuation(plainText)
            print("\n",noSymbol, "\n")
        elif menu == 4:
            reversal = reverseString(plainText)
            print("\n",reversal, "\n")
        elif menu == 5:
            noSpaces = removeSpaces(plainText)
            print("\n",noSpaces, "\n")
        elif menu == 6:
            print("\n",stats, "\n")
        elif menu == 7:
            freqq = frequencyAnalysis(plainText)
            print("\n",freqq, "\n")
        elif menu == 8:
            advfreqq = advancedFrequencyAnalysis(plainText)
            print("\n",advfreqq, "\n")
        else:
            print("PLEASE MAKE A SELECTION") #Menu repeats if no selection is made
            menu = int(input(textManipulationMenuFormat))
    else: #Main menu repeats if no selection is made between 1 or 2
        print("PLEASE MAKE A SELECTION")
        mainMenu = int(input(mainMenuFormat))