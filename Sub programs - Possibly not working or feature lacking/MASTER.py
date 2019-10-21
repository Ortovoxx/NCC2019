import random
freqWords = ["the","be","of","and","a","to","in","he","have","it","that","for","they","i","with","as","not","on","she","at","by","this","we","you","do","but","from","or","which","one","would","all","will","there","say","who","make","when","can","more","if","no","man","out","other","so","what","time","up","go","about","than","into","could","state","only","new","year","some","take","come","these","know","see","use","get","like","then","first","any","work","now","may","such","give","over","think","most","even","find","day","also","after","way","many","must","look","before","great","back","through","long","where","much","should","well","people","down","own","just","because","good","each","those","feel","seem","how","high","too","place","little","world","very","still","nation","hand","old","life","tell","write","become","here","show","house","both","between","need","mean","call","develop","under","last","right","move","thing","general","school","never","same","another","begin","while","number","part","turn","real","leave","might","want","point","form","off","child","few","small","since","against","ask","late","home","interest","large","person","end","open","public","follow","during","present","without","again","hold","govern","around","possible","head","consider","word","program","problem","however","lead","system","set","order","eye","plan","run","keep","face","fact","group","play","stand","increase","early","course","change","help","line"]
alphabetASCII = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
alphabetCHARACTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def convertToASCII(text): #Converts an array of characters into an array of their ASCII equivilant numbers
    perm = 0
    while perm < len(text):
        text[perm] = ord(text[perm])
        perm = perm + 1
    return text
def convertToCHARACTER(text): #Converts an array of ASCII equivilant numbers into an array of their ASCII equivilant characters
    perm = 0
    while perm < len(text):
        text[perm] = chr(text[perm])
        perm = perm + 1
    return text
def substitionKeyCipher(userCipherText,userKey): #maps a ciphertext to plaintext according to the key given to it
    cipherText = convertToASCII(list(userCipherText)) #Converting cipher to numbers
    key = convertToASCII(list(userKey)) #Converting key to numbers
    def switchChar(cipherChar): #Switches a single character from its chiphertext to its plaintext
        alphaPerm = 0
        newChar = 0
        while alphaPerm < len(alphabetASCII):
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

#ADD TO THE KEY GENERTAION FUNCTION
#WORD KEYS
#NO DUPLICATION KEYS
#KEY STORAGE - high intensity

def keyGeneration(): #generates a key
    def search(randomNo,key): #Searches to see if there are repeats
        position = 0
        found = False
        while position < len(key) and not found:
            if key[position] == randomNo:
                found = True
            position = position + 1
        return found
    key = []
    perms = 0
    while perms < len(alphabetASCII):
        randomNo = random.randint(97, 122)
        repeat = search(randomNo,key) #Ensures each letter is unique
        if repeat == False:
            key.append(randomNo)
            perms = perms + 1
    finalKey = "".join(convertToCHARACTER(key))
    return finalKey




while True == True:
    userCipher = input("CIPHERTEXT: ")
    userKeyCount = int(input("KEY NUMBER: "))
    n = 0
    while n < userKeyCount:
        userKey = keyGeneration()
        cipherOut = substitionKeyCipher(userCipher,userKey)
        cipherOutKeyOut ='''

PLAINTEXT:
{cipherOut}
KEY:
{userKey}

'''.format(cipherOut = cipherOut, userKey = userKey)
        if clearScoreEnglish(cipherOut) > 10:
            print(cipherOutKeyOut)
        n = n + 1







    
