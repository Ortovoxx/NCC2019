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
        if ord(characters[n]) != 32:
            charactersNoSpace.append(characters[n])
        n = n + 1
    charactersNoSpaceJoint = "".join(charactersNoSpace)
    return charactersNoSpaceJoint

def reverseString(string): #Reverses the text
    return string[::-1]
 
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
 
   Characters:     {characterCount}
   Symbols:        {symbolCount}
   Uppercases:     {upperCount}
   LowerCases:     {lowerCount}
   Numbers:        {numberCount}
   Spaces:         {spaceCount}
   Words:          {wordCount}
 
 ========================================'''.format(characterCount = characterCount, symbolCount = symbolCount, upperCount = upperCount, lowerCount = lowerCount, numberCount = numberCount, spaceCount = spaceCount, wordCount = wordCount)
 
while True == True: #Asks for user input and allows for return to be entered to use the previous cipher again
    plainText = input("*********** INPUT YOUR TEXT: ***********\n")
    if plainText == "":
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
    menu = int(input('''****************************************
 
 1  -  Convert to lowercase
 2  -  Convert to uppercase
 3  -  Remove punctuation
 4  -  Reverse text
 5  -  Remove spaces
 6  -  Statistics
 7  -  Frequency analysis
 8  -  Advanced frequency analysis

**************** SELECT: ***************
'''))
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
        print("PLEASE MAKE A SELECTION")
        menu = int(input('''****************************************
 
 1  -  Convert to lowercase
 2  -  Convert to uppercase
 3  -  Remove punctuation
 4  -  Reverse text
 5  -  Remove spaces
 6  -  Statistics
 7  -  Frequency analysis
 8  -  Advanced frequency analysis

**************** SELECT: ***************
'''))
