def substitionKeyCipher(userCipherText,userKey):
    alphabet = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
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
    cipherText = convertToASCII(list(userCipherText)) #Converting cipher to numbers
    key = convertToASCII(list(userKey)) #Converting key to numbers
    def switchChar(cipherChar): #Switches a single character from its chiphertext to its plaintext
        alphaPerm = 0
        newChar = 0
        while alphaPerm < len(alphabet):
            if cipherChar == key[alphaPerm]:
                newChar = alphabet[alphaPerm]
            alphaPerm = alphaPerm + 1
        return newChar
    textPerm = 0
    switchedCipher = []
    while textPerm < len(cipherText): #Goes through each character one by one and sends to the function which converts cipher to plain
        switchedCipher.append(switchChar(cipherText[textPerm]))
        textPerm = textPerm + 1
    switchedCipherStr = "".join(convertToCHARACTER(switchedCipher))
    return switchedCipherStr
 
while True == True:
    userCipher = input("Ciphertext:")
    userKey = input("Key:")
    cipherOut = substitionKeyCipher(userCipher,userKey)
    print(cipherOut)

'''


CIPHER: rbo rpktigo vcrb bwucja wj kloj hcjd km sktpqo cq rbwr loklgo vcgg cjqcqr kj skhcja wgkja wjd rpycja rk ltr rbcjaq cj cr
KEY: wisdomabcnzghjklfpqrtuveyx

OUTPUT: the trouble with having an open mind of course is that people will insist on coming along and trying to put things in it


'''
