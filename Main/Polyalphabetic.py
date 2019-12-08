#==============================================================================================================================================================
#                                                                          Euan Caskie 
#
#                                                                 National Cipher Challenge 2019
#==============================================================================================================================================================

############# IMPORTANT INFO BEFORE USING THIS PROGRAM #############
# Ensure you have an ngram.txt file in the correct directory:
loadEnglishNgramDirectory = "/Users/Euan/Desktop/NCC2019/Cryptanalysis/Text_training_data"
loadKeyWordsDirectory = "/Users/Euan/Desktop/NCC2019/Cryptanalysis"
outputFilesHere = "/Users/Euan/Desktop/NCC2019/Out"
# All functions should transfer data using lowercase no space no punctuation strings

#########  TEST CIPHERS TO TRY AND SOLVE  #########
#rborpktigovcrbbwucjawjklojhcjdkmsktpqocqrbwrloklgovcggcjqcqrkjskhcjawgkjawjdrpycjarkltrrbcjaqcjcr
#TjfBsppxrippxrssqjubijvpdhjespojwreybszrhmdhsrwpsrsbpenbaqjwraaibjyspsqjsjksRsubwhsbszrhqrwysphrvbusqrszrhrcdfpwrujrsdwjreyepwtriivBzpdiyrhhdtjcdfcdsbshjjtjypyysqrsbszrhsqjpeivubijsqrszrhruujnsjyhpBrhxjyrwpdeysphjjburevpejqryhjjerevsqbefhbtbirw.Bssdwehpdssqrssqbhzrhepssqjubwhserobfrsbpeawpcijtspqbssqjawpfwrttj.FjejwjapwsjyrtrmpwbhhdjzbsqsqjfdbyrenjawpfwrttjupwHeppavpesqjRapiipSjetbhhbpezqbnqnpdiyrfrbeqrojnrdhjyrtrmpwawpcijt.Upwhptjwjrhpesqjawpfwrttjnpeswpiibefsqjireybefwryrwzrhe’sdayrsjyzbsqsqjuibfqsairereybuFjejqrye’swrbhjysqrszbsqBojwhpesqjesqjcpvhtbfqsqrojqrywjriswpdcijfjssbefcrnx.Bippxjysqwpdfqsqjnptarevubijhreyupdeyrepsqjwpupdwtvhsjwbpdhivupwtrssjywjapwsh:sqjtjtpbeupwtbefsqjtrcpdssqjnqrefj,zqbnqjkairbehzqvsqjawpfwrttjejojwfpsdayrsjy.Sqbhsbtjsqjnbaqjwzrhreruubejhqbus,hphibfqsivqrwyjwspnwrnx,cdsepsqbefhjwbpdh.Hsbii,bsbhtdnqijhhibxjivsqrsbszrhrcdfsqrssbtj,reyberevnrhjszbnjbhspptdnqpurnpbenbyjenj.Bsybyhsrwstjzpeyjwbefzqvsqjhjnpeynbaqjwzrhjrhbjwspnwrnxsqresqjubwhs,cdssqjeBwjribhjysqrssqjruubejhqbuszrhspptdnqpurfbojrzrv.Rwpsrsbpenbaqjwwjriivnpdiymdhscjrejenpybefjwwpw,cdssqjruubejhqbusbhspphpaqbhsbnrsjyupwrtbhsrxj,hpzqpjojwtrefijysqjwjapwshtdhsqrojwjribhjysqjvqrytryjrcbspurejwwpwzbsqsqjubwhspejreyswbjyspnpojwsqjbwhsjahzbsqsqjhjnpey.Bsbhqrwysphjjsqbhrhrevsqbefpsqjwsqrerssjtasjyhrcpsrfj,cdsBrtepshdwjzqrssqjtpsbojnpdiycj.Bypdcsbsbhajwhperi.SqjRapiipSjereyJijojenwjzhype’spojwira,hpjbsqjwhptjpejqrhrfwdyfjrfrbehssqjzqpijRhswperdsnpwahpwsqjvrwjswvbefspyjwrbisqjRapiipawpfwrttj.BsnpdiycjsqjHpobjshBhdaaphj.Rsubwhs,BsqpdfqssqrssqjbwzbiibefejhhsphqbussqjIDER-UBUSJJEpwcbshqpzjysqrssqjvzjwje’sarwspubs,cdshptjpejbesqjHsrsjYjarwstjesapbesjypdssqrssqjvtbfqsmdhsqrojqryrfdbisvnpehnbjenj,pwcjjexjjespybhsrenjsqjthjiojhpenjsqjaipszrhybhnpojwjy.Brthsbiiepshdwj.Besqjtjresbtj,npdiyvpdsrxjrippxrssqjnptadsjwubijhsphjjzqptbfqsqrojqryrnnjhhspcpsqtjtph,reyzqptbfqsqrojqrysqjpaapwsdebsvreytjrehspypnspwsqjt?BrtuivbefcrnxspIrefijvspebfqssphjjbusqjHsrsjYjarwstjesqrojrevbyjrhzqrstbfqscjfpbefpeEjbihrbyqjnpdiyuivtjdabepejpusqjERHRnqrhjairejhzqbnqbhhptjsqbefBqrojcjjexjjespswv.BzbiinriivpdbuBfjsrevsqbef
#xqhhoyqcdejikhuyvoekmuhusefyutydjejxucuceqrekjhusudjuludjirkjxuhuyiqikccqhojmetqoiqweqdevvtkjowkytqdsuevvysuhqbuhjutcyiiyedsedjhebjeqfejudjyqbfherbucmyjxjxuqfebbevbywxjjxufbqdduttuisudjjhqzusjehoqffuqhutjeruhkddydwedqsebbyiyedsekhiumyjx
#WKMPCZKXDVSYEZUKYLTVICYFKBVDDNKZKXDVMYXOBPKLPXMDNKCDVLLVXTDBIPXMDYMVEMKDNKWYYTDNKBKIYEVBKBPMNDDNKNVGRCVBKMKDDPXMZBKDDIBKCDUKCCVXTNVFKWYBKYBUKCCTKSPTKTVUBKVTIDNVDDNKCYFPKDCVBKDYOUVWKLYBBKSKXDKFKXDCYXDNKVZYUUYZBYMBVWWKCYWKYLDNKMKXKBVUCTYXDXKKTWESNYLVXKHSECKDYDEBXEZDNKNKVDOEDIYETYXDMKDLYEBCDVBCGPDNYEDEXTKBCDVXTPXMDNKXKKTLYBZYUPDPSVUCEZZYBDVXTDNKBKNVCOKKXVSYXSKBDKTGNPCZKBPXMSVWZVPMXDYSYXFPXSKDNKZBKCPTKXDDYDVRKVCDBYXMUPXKDNKWYCDCDBPTKXDVBKSVUUPXMLYBVUVBMKOEPUTEZYLLYBSKCVUYXMDNKOYBTKBGPDNKVCDMKBWVXIVCVCNYGYLCDBKXMDNVBMEPXMDNVDDNKVDDVSRYXDNKCZVSKZBYMBVWWKWECDNVFKOKKXVEDNYBPCKTOIDNKZYUPDOEBYDNVDWVRKCXYCKXCKDYWKLPBCDDNKBECCPVXCVBKWYBKUPRKUIDYDBIDYGPXDNKZBYZVMVXTVGVBDNVXDYBPCRSYXLUPSDVXTCKSYXTDNKCVOYDVMKPLDNVDPCGNVDPDPCPCXDCYZNPCDPSVDKTKXYEMNLYBVRMOYZKBVDPYXOEDPDPCNVBTDYSYXFPXSKDNKMKXKBVUCDNVDDNVDPCDBEKCYWKYLDNKWYBKSVEDPYECZUVXXKBCWYCDUIDNYCKGNYVSDEVUUILYEMNDPXDNKUVCDGVBNVFKWVXVMKTDYOUYSRDNKOEPUTEZZBYZYCPXMVXKGDBVXSNKYLGVBMVWKCPXCDKVTWYOPUPCPXMDNVDGVIPCCDPUUVZBYFYSVDPYXOEDPCUKCCUPRKUIDYVSSPTKXDVUUIDBPMMKBVGVBKCZKSPVUUIPLGKXYDPLIZVFUYFCRIPXVTFVXSKVUUDNKCVWKWIYGXDPWKPXOKBUPXSYXFPXSKTWKGKNVFKDYDBKVTFKBICYLDUIDNKBKCYPNKVTKTYFKBDYUVXMUKIVXTSYXFPXSKTDNKWDYCEMMKCDVXVUDKBXVDPFKGKGPUUCDKZEZPXCZKSDPYXCVDSNKSRZYPXDSNVBUPKDYWVRKPDNVBTKBLYBCYFPKDVMKXDCDYSBYCCVXTSBVXREZDNKDKELKUCOKBMUPCDKXPXMYZKBVDPYXDYCKKPLDNVDDEBXCEZVXIDNPXMBKUVDKTPVWVUCYMYPXMDYCKXTVSYEZUKYLYEBOKCDYFKBDYOVPRYXEBDYDBIVXTLPXTYEDGNVDPCMYPXMYXDNKBKDNKCYFPKDCVBKZBKDDICKSBKDPFKVOYEDDNKPBYGXCZVSKZBYMBVWWKVXTGPDNYEDDNKGYBUTCZBKCCGVDSNPXMGKTYXDBKVUUINVFKVSUKVBZPSDEBKYLDNKPBZBYMBKCCYBDNKPBZUVXCEXUKCCDNKIVBKSUYCKDYZEDDPXMDNKPBYGXWKXYXDNKWYYXPSVXDCKKGNVDDNKINVFKDYMVPXGPDNGNVDCKKWCDYOKVLVPBUITPCYBMVXPCKTVDDKWZDDYTKBVPUYEBCZVSKZBYMBVWWKOEDPGYEUTCDPUUUPRKDYRXYGGNVDDNKIVBKEZDYRKKZVSUYCKKIKYXDNKWPCCPYXZUVXXPXMVXTUKDWKRXYGPLIYENKVBVXIDNPXMGYBBIPXMPGPUUOKOVSRVOYEDVGKKROKLYBKDNKUVEXSNNVBBI
#pmpafxaikkitprdsikcplifhwceigixkirradfeirdgkipgigudkcekiigpwrpucikceiginasikwduearrxiiqepcceindgmieinpwdfprduppcedoikiqiasafmfddfipfgmdafmfdteiki

#==============================================================================================================================================================
#                                                                  VARIABLES, CONSTANTS AND FORMATTING - DO NOT EDIT
#==============================================================================================================================================================

#Modules to imports
import random
import os
import math
import time
import re

#Menu and input formats
cipherSolverInputFormat = '''*************** CIPHERTEXT: **************
'''
textManipulationInputFormat = '''*********** INPUT YOUR TEXT: ***********
'''

######## ALPHABET LISTS ########
alphabetASCII = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
alphabetCHARACTER = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabetMorse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
numbersMorse = ["-----",".----","..---","...--","....-",".....","-....","--...","---..","----."] # 0 1 2 3 4 5 6 7 8 9
#all in expected % occurance
englishLetterFrequency = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]
englishLetterFrequencySorted = [12.702,9.056,8.167,7.507,6.966,6.749,6.327,6.094,5.987,4.253,4.025,2.782,2.758,2.406,2.360,2.228,2.015,1.974,1.929,1.492,0.978,0.772,0.153,0.150,0.095,0.074]
#The above list numbers map to the following letters (in order) -- E T A O I N S H R D L C U M W F G Y P B V K J X Q Z

def loadEnglishNgram(): #loads a ngram file to a ditionary
        os.chdir(loadEnglishNgramDirectory) #path of ngram file to load make sure .txt file is in this folder MAKE SURE NGRAMS ARE LOWER CASE
        quadramDitionaryEnglish = {}
        with open("ngram.txt", "r") as f:
            for line in f: # goes through each line and splits it into a 2 item list
                quadramList = line.split()
                quadramDitionaryEnglish[quadramList[0]] = float(quadramList[1]) # puts the list into a ditionary
        return quadramDitionaryEnglish
def loadKeyWords(): #loads a keyword file to a list
        os.chdir(loadKeyWordsDirectory) #path of ngram file to load make sure .txt file is in this folder MAKE SURE NGRAMS ARE LOWER CASE
        keyWords = []
        with open("keywords.txt", "r") as f:
            for line in f:
                keyWords.append(line.strip("\n")) # Adds the keywords to a list and removes the newline character
        return keyWords
def export(): #exports brute forced ciphers to a text file for easy access later
    os.chdir(outputFilesHere) #path of output file to save to
    with open("output.txt", "a") as f:
        for key in outputExportDitionary:
            f.write(key +"\n") # Writes the key used to solve the cipher
            f.write(outputExportDitionary[key]+"\n") # Writes the actual solved cipher
keyWords = loadKeyWords() #Calls the above functions to load them into memory from a file - Comment out if you dont need them and want to go faster
ngramDitionaryEnglish = loadEnglishNgram() # ''
outputExportDitionary = {}

#==============================================================================================================================================================
#                                                       TEXT MANIPULATION AND REPEATED USE FUNCTIONS - DO NOT EDIT
#==============================================================================================================================================================

def convertToASCII(textList): #Converts an list of characters into an list of their ASCII equivalent numbers
    output = []
    for n in textList: #goes through each list index and turns it from Character to ASCII
        output.append(ord(n))
    return output
def convertToCHARACTER(textList): #Converts an list of ASCII equivalent numbers into an list of their ASCII equivalent characters
    output = []
    for n in textList: #goes through each list index and turns it from ASCII number to Character
        output.append(chr(n))
    return output
def BINtoDEC(binary): # Binary to Decimal converter
    return int(str(binary),2)
def DECtoBIN(decimal): # Decimal to Binary converter
    return int(re.sub("0b","",str(bin(decimal))))
def DECtoHEX(decimal): # Decimal to Hexadecimal converter
    return re.sub("0x","",str(hex(decimal)))
def HEXtoDEC(hexN): # Hexadecimal to Decimal converter
    return int(str(hexN),16)
def DECtoOCT(decimal): # Decimal to Octal converter
    return int(re.sub("0o","",str(oct(decimal))))
def OCTtoDEC(octal): # Octal to Decimal converter
    return int(str(octal),8)
def formatString(string): #removes everything apart from a-z lower case from a string
    return "".join(re.findall("[a-z]",string))
def reverseString(string): #Reverses the text
    return string[::-1]
def spliting(string,separator): # Returns a list from a string which has been split with a set separator
    return re.split(separator,string)
def search(itemToCheckFor,listToSearchFrom): #LINEAR SEARCH GLOBAL FUNCTION - Searches to see if there are repeats for random and keyword keys returns T or F
    position = 0
    found = False
    while position < len(listToSearchFrom) and not found:
        if listToSearchFrom[position] == itemToCheckFor:
            found = True
        position += 1
    return found
def shiftRight(listToMove,numberToMoveBy): # Shifts a list one place to the right including wrap arrounds
    index = 0
    while index < numberToMoveBy:
        position = listToMove.pop()
        listToMove.insert(0, position)
        index += 1
    return listToMove
def substitionKeyCipher(userCipherText,userKey): #maps a ciphertext to plaintext according to the key given to it
    cipherText = convertToASCII(list(userCipherText)) #Converting cipher to numbers
    key = convertToASCII(list(userKey)) #Converting key to numbers
    def switchChar(cipherChar): #Switches a single character from its chiphertext to its plaintext
        alphaPerm = newChar = 0
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
    return "".join(convertToCHARACTER(switchedCipher))
def characterFrequency(encryptedText):
    frequencies = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in encryptedText: #iterates through each character in encrypted_cipher text
        index = 0 #element index set at 0 #WHEN data at index (character in encrypted text) does not equal first element #AND the alphabet index is less than 25, (i.e all letters encompassed only):
        while i != letter[index] and index < 25: #THEN increment pos index ++, avoids indexing greater than alphabet list
           if index <= 24:
               index += 1
        else: #increments relative index dependant upon character contained within i
            if i == letter[index]:
                frequencies[index] = frequencies[index] + 1 #if character in encrypted_text is a space,data @ alphabet[26] ++:       
    return frequencies
def characterFrequencyProbability(encryptedText):
    frequencies = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    probability = []
    for i in encryptedText: #iterates through each character in encrypted_cipher text
        index = 0 #element index set at 0 #WHEN data at index (character in encrypted text) does not equal first element #AND the alphabet index is less than 25, (i.e all letters encompassed only):
        while i != letter[index] and index < 25: #THEN increment pos index ++, avoids indexing greater than alphabet list
           if index <= 24:
               index += 1
        else: #increments relative index dependant upon character contained within i
            if i == letter[index]:
                frequencies[index] = frequencies[index] + 1 #if character in encrypted_text is a space,data @ alphabet[26] ++:
    for n in frequencies:
        x = round((n / len(encryptedText)),5)
        probability.append(x)
    return probability
def indexOfCoincidence(text): #String input to calculate the Index of Coincidence of a text
    def letter(letterCount,textLength):
        letterValue = (letterCount / textLength)*((letterCount - 1)/(textLength - 1))
        return letterValue
    IoCLIST = []
    alphaIndex = 0
    textList = convertToASCII(list(text))
    textLength = len(textList)
    while alphaIndex < 26:
        letterCount = textList.count(alphaIndex + 97)
        IoCLISTStore = (letter(letterCount,textLength))
        IoCLIST.append(IoCLISTStore)
        alphaIndex += 1
    return sum(IoCLIST)
def chiSquaredStat(text): #String input which calculates the chi-squared statistic of a text
    def letter(realLetterCount,expectedLetterCount):
        letterValue = ((realLetterCount - expectedLetterCount)**2) / expectedLetterCount
        return letterValue
    chiSquaredLIST = []
    alphaIndex = 0
    textList = convertToASCII(list(text))
    textLength = len(textList)
    while alphaIndex < 26: 
        realLetterCount = textList.count(alphaIndex + 97)
        expectedLetterCount = textLength * (englishLetterFrequency[alphaIndex]) / 100 #Compares it against an english distribution probability
        chiSquaredLISTStore = letter(realLetterCount,expectedLetterCount)
        chiSquaredLIST.append(chiSquaredLISTStore)
        alphaIndex += 1
    return sum(chiSquaredLIST)
def ngramFitness(userCiperText):
    def ngramExtraction(userCiperText): #Finds quadgrams from a ciphertext
        cipherText = list(userCiperText)
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
    return sum(logAB)
def relationToEnglishFrequency(cipherTextFrequency): # Finds the difference between a ciphertext frequency ( % ) and english frequency and outputs a score 
    index = 0
    lists = []
    while index < 25:
        difference = round(englishLetterFrequency[index] - (cipherTextFrequency[index])*100,10)
        lists.append(difference)
        index+=1
    score = sum(lists)
    return round(score,10)
def addPadding(cipher,key): # pads a transposition ciphertext with a padding character of X
    cipher = list(cipher)
    lengthCipher = len(cipher)
    remainder = lengthCipher % key # Finds how many padding characters to add
    if remainder == 0: #If the ciphertext length is divisible by the key perfectly then no padding is needed
        return "".join(cipher)
    else:
        addPad = 0
        while addPad <= remainder: # Loops round the cipher text array adding a padding character each time
            cipher.append("x") # The padding character
            addPad+=1
        return "".join(cipher)
def textBlock(textIN): #Takes a plaintext string input and returns a list with a sublist of blocked characters
    n = 3 #The size of the text blocks
    text = list(textIN)
    length = len(text)
    blockedText = []
    remainder = length % n
    index = addPad = 0
    if remainder != 0:
        while addPad <= remainder: # Loops round the cipher text array adding a padding character each time
            text.append("x") # The padding character
            addPad+=1
    while index < length:
        blocked = []
        blocking = 0
        while blocking < n:
            add = text[blocking + index]
            blocked.append(add)
            blocking+=1
        blockedText.append("".join(blocked))
        index+=n
    return blockedText
def textReplace(textBlockIN,find,replace):#Takes an array with strings of blocked characters and repalces them with others
    textBlockOUT = []
    for n in textBlockIN:
        new = n.replace(find,replace)
        textBlockOUT.append(new)
    return textBlockOUT
def factors(textIN):
    text = list(textIN)
    length = len(text)
    factorList = [length]
    for i in range(1,length):
        if length % i == 0:
            factorList.append(int(i))
    #print(sorted(factorList))
    #print(length)
    return sorted(factorList)

#==============================================================================================================================================================
#                                                            CIPHER SOLVING - EDITABLE
#==============================================================================================================================================================

ciphertext = ""
key = "hello"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def decrypt(ciphertext,key):
    plaintext = ''
    for i in range(len(ciphertext)):
        fre  = len(key)
        gg = i%fre
        p = ALPHABET.index(ciphertext[i])
        k = ALPHABET.index(key[gg])
        c = (p - k) % 26
        plaintext += ALPHABET[c]
    return plaintext
key = ['']*3
for key[0] in ALPHABET:
    for key[1] in ALPHABET:
        for key[2] in ALPHABET:
            pt = decrypt(ciphertext,key)
            fit = ngramFitness(pt)
            if fit > -10:
                break
            else:
                continue
            break
        else:
            continue
    break
plaintext = decrypt(ciphertext,key)






#==============================================================================================================================================================
#                                                   USER INPUT / OUTPUT                   MAIN PROGRAM
#==============================================================================================================================================================

userKey = "abcdefghijklmnopqrstuvwxyz" #Sets a defult user key ~~~~WARNING~~~~ Wont show error if there is not a key generated as this one will take over ~~~~WARNING~~~~
keyIterations = REPLACEME123 = 0
exporting = False

#########  Turn each function on or off  #########

# KEY WORD:
vigStart = True

# DECLARE USERCIPHER HERE AND COMMENT OUT THE USER INPUT IF YOU ARE WORKING ON THE SAME CIPHER
userCipherNoFormatBypass = ""
userCipher = formatString((userCipherNoFormatBypass).lower())

while True: #Loops the entire program
    #userCipher = formatString((input(cipherSolverInputFormat)).lower()) # ensures all ciphertext given to functions is correclty formatted
    #########################################################
    #           Calling different deciphering functions
    #########################################################
    while keyIterations < keyIterations + 1:
        if vigStart == True: #Ceaser shifts done 26 times
            cipherOut = "test"
        ###############
        if exporting == True:
            export()
            print("exported!")
        keyIterations += 1
        #########################################################
        #                   Text statistics
        #########################################################
        ### Choose which scoring system you want to rank texts by: ###
        
        #indexOfCoincidenceText = round(indexOfCoincidence(cipherOut),10)
        #chiSquaredText = round(chiSquaredStat(cipherOut),10)
        #ngramScore = ngramFitness(cipherOut)
        #relationScore = relationToEnglishFrequency(characterFrequencyProbability(cipherOut))

        # if relationScore < 0.05 and relationScore > -0.05:
        ngramScore = -400
        if ngramScore > -40: # Change this number here the closer to 0 the less it will accept and print
            indexOfCoincidenceText = round(indexOfCoincidence(cipherOut),10)
            chiSquaredText = round(chiSquaredStat(cipherOut),10)
            ngramScore = ngramFitness(cipherOut)
            relationScore = relationToEnglishFrequency(characterFrequencyProbability(cipherOut))
            outputExportDitionary[userKey] = cipherOut
            cipherOutKeyOut ='''
================== PLAINTEXT: ==================
{printedCipherOut}
===================== KEY: =====================
{printedUserKey}
================= STATISTICS: ==================
Number of keys              {printedAttempts}
log Ngram Score             {printedNgramScore}
Index Of Coincidence        {printedIoC}
Chi Squared                 {printedChi}
English Frequency Relation  {printedRelationScore}
'''.format(printedCipherOut = cipherOut,printedUserKey = userKey,printedNgramScore = ngramScore,printedAttempts = keyIterations,printedIoC = indexOfCoincidenceText, printedChi = chiSquaredText,printedRelationScore = relationScore)
            print(cipherOutKeyOut)
