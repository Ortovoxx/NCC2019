import random
def keyGeneration():
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
    
    while perms < len(alphabet):
        randomNo = random.randint(97, 122)
        repeat = search(randomNo,key) #Ensures each letter is unique
        if repeat == False:
            key.append(randomNo)
            perms = perms + 1
    finalKey = "".join(convertToCHARACTER(key))
    return finalKey

n = 0
while n < 1000:
    x = keyGeneration()
    print(x)
    n = n + 1
    
