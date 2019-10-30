import random
alphabetASCII = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
alphabetCHARACTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#IN %
englishLetterFrequency = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]
englishLetterFrequencySorted = [12.702,9.056,8.167,7.507,6.966,6.749,6.327,6.094,5.987,4.253,4.025,2.782,2.758,2.406,2.360,2.228,2.015,1.974,1.929,1.492,0.978,0.772,0.153,0.150,0.095,0.074]
#Probabilty /1
englishLetterFrequencyProbability = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]
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



#xqhho y qc dej ikhu yv oek muhu sefyut yd je jxu cuce qrekj husudj uludji rkj xuhu yi q ikccqho jme tqoi qwe qd evvtkjo wkytqdsu evvysuh qbuhjut cyiiyed sedjheb je q fejudjyqb fherbuc myjx jxu qfebbe vbywxj jxu fbqddut tuisudj jhqzusjeho qffuqhut je ru hkddydw ed q sebbyiyed sekhiu myjx

def iterativeSolving(userCipherText):
    parentKey = randomKey() #parent Key is generated using frequency analysis
    decipher = substitionKeyCipher(userCipherText,parentKey) #solves parent cipher using the parent key
    parentScore = chiSquaredStat(decipher) #Gets the text fitness of this ciphertext
    iteration = 0
    while iteration < 1000:
        a = random.randint(0,25) #2 random letters (numbers) generated
        b = random.randint(0,25)
        childKeyArray = list(parentKey) #converts parent key string into a child array
        childKeyArray[a],childKeyArray[b] = childKeyArray[b],childKeyArray[a] # swap two characters in the child
        childKey = "".join(childKeyArray) #converts child key array into a string
        decipher = substitionKeyCipher(userCipherText,childKey) #deciphers the ciphertext with the new jumbled key
        childScore = chiSquaredStat(decipher) #gets the text fitness score of the new ciphertext
        if childScore < parentScore: # if the child was better, replace the parent with it. Else dont...
            parentScore = childScore
            parentKey = childKey
            iteration = 0 #reset the iteration count to 0 as it is getting better and is not at a local minimum
        iteration = iteration + 1
    if childScore < 50:
        return decipher

userCipherText = input("text: ")
x = iterativeSolving(userCipherText)
print(x)