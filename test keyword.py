freqWords = ["the","of","to","and","a","in","is","it","you","that","he","was","for","on","are","with","as","I","his","they","be","at","one","have","this","from","or","had","by","hot","but","some","what","there","we","can",
         "out","other","were","all","your","when","up","use","word","how","said","an","each","she","which","do","their","time","if","will","way","about","many","then","them","would","write","like","so","these","her","long",
         "make","thing","see","him","two","has","look","more","day","could","go","come","did","my","sound","no","most","number","who","over","know","water","than","call","first","people","may","down","side","been","now","find",
         "any","new","work","part","take","get","place","made","live","where","after","back","little","only","round","man","year","came","show","every","good","me","give","our","under","name","very","through","just","form",
         "much","great","think","say","help","low","line","before","turn","cause","same","mean","differ","move","right","boy","old","too","does","tell","sentence","set","three","want","air","well","also","play","small","end",
         "put","home","read","hand","port","large","spell","add","even","land","here","must","big","high","such","follow","act","why","ask","men","change","went","light","kind","off","need","house","picture","try","us","again",
         "animal","point","mother","world","near","build","self","earth","father","head","stand","own","page","should","country","found","answer","school","grow","study","still","learn","plant","cover","food","sun","four",
         "thought","let","keep","eye","never","last","door","between","city","tree","cross","since","hard","start","might","story","saw","far","sea","draw","left","late","run","dont","while","press","close","night","real",
         "life","few","stop","open","seem","together","next","white","children","begin","got","walk","example","ease","paper","often","always","music","those","both","mark","book","letter","until","mile","river","car","feet",
         "care","second","group","carry","took","rain","eat","room","friend","began","idea","fish","mountain","north","once","base","hear","horse","cut","sure","watch","color","face","wood","main","enough","plain","girl",
         "usual","young","ready","above","ever","red","list","though","feel","talk","bird","soon","body","dog","family","direct","pose","leave","song","measure","state","product","black","short","numeral","class","wind",
         "question","happen","complete","ship","area","half","rock","order","fire","south","problem","piece","told","knew","pass","farm","top","whole","king","size","heard","best","hour","better","true","during","hundred",
         "am","remember","step","early","hold","west","ground","interest","reach","fast","five","sing","listen","six","table","travel","less","morning","ten","simple","several","vowel","toward","war","lay","against",
         "pattern","slow","center","love","person","money","serve","appear","road","map","science","rule","govern","pull","cold","notice","voice","fall","power","town","fine","certain","fly","unit","lead","cry","dark",
         "machine","note","wait","plan","figure","star","box","noun","field","rest","correct","able","pound","done","beauty","drive","stood","contain","front","teach","week","final","gave","green","oh","quick","develop",
         "sleep","warm","free","minute","strong","special","mind","behind","clear","tail","produce","fact","street","inch","lot","nothing","course","stay","wheel","full","force","blue","object","decide","surface","deep",
         "moon","island","foot","yet","busy","test","record","boat","common","gold","possible","plane","age","dry","wonder","laugh","thousand","ago","ran","check","game","shape","yes","hot","miss","brought","heat","snow",
         "bed","bring","sit","perhaps","fill","east","weight","language","among","nasa","harry","cipher","nuclear","war","catastrophe","apollo","one","two","three","four","five","six","seven","eight","nine","ten","eleven",
         "twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eightteen","nineteen","twenty","apollo","lunar","mission","phase","orbit","orbital","prime","objective","spacecraft","meg","file","luna","programme",
         "state","deparment","united","states","america","usa","uk","britain","americas","gene","conscience","plot","navigation","niel","file","files","coincidence","once","twice","wisdom","launch",]
alphabetASCII = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]

def search(randomNo,key): #Searches to see if there are repeats
        position = 0
        found = False
        while position < len(key) and not found:
            if key[position] == randomNo:
                found = True
            position = position + 1
        return found
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
'''
def randomKey(): #generates a random key
    perms = 0
    while perms < len(alphabetASCII): #Ensures 26 letters in the alphabet
        randomNo = random.randint(97, 122)
        repeat = search(randomNo,key) #Ensures each letter is unique
        if repeat == False:
            key.append(randomNo)
            perms = perms + 1
'''

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
def keyWord(perms):
    print(perms)
    alphaPerm = 0
    while perms < len(freqWords):
        
        keyWordASCII = convertToASCII(list(freqWords[perms]))
        #x = "".join(convertToCHARACTER(keyWordASCII))
        #print(x)
        while alphaPerm < len(alphabetASCII):
            repeat = search(alphabetASCII[alphaPerm],keyWordASCII) #Ensures each letter is unique
            if repeat == False:
                keyWordASCII.append(alphabetASCII[alphaPerm])
            alphaPerm = alphaPerm + 1
        
    finalKey = "".join(convertToCHARACTER(keyWordASCII))
    print(finalKey)
    return finalKey

userKey = "abcdefghijklmnopqrstuvwxyz"
while True == True:
    n = 0
    userCipher = input("CIPHERTEXT: ")
    while n < 10000:
        print(n)
        userKey = keyWord(n)
        cipherOut = substitionKeyCipher(userCipher,userKey)
        cipherOutKeyOut ='''

PLAINTEXT:
{cipherOut}
KEY:
{userKey}

'''.format(cipherOut = cipherOut, userKey = userKey)
        if clearScoreEnglish(cipherOut) > 5:
            print(cipherOutKeyOut)
        n = n + 1
