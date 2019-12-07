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

#==============================================================================================================================================================
#                                                            CIPHER SOLVING - EDITABLE
#==============================================================================================================================================================

'''
# columnar transposition cipher
ciphertext = input("Enter ciphertext here")
ciphertextlength = len(ciphertext)
ciphertextarray = list(ciphertext)
print(ciphertextarray)
#gets the number of columns used in the transposition P.s make sure that the ciphertextlength is exactly divisible by the columnumber. If not u can always add a few random characters to even it out.
columnnumber = int(input("number of columns"))
# creates the same number of arrays as columns
columns = [[" "] for j in range (0,columnnumber)] 
columnlength = int(ciphertextlength/columnnumber)
i = 0
j = 0
# splits the ciphertext into columns and iterates through until no more letters are left
while j < columnnumber and i < ciphertextlength:
  columns[j] = [ciphertextarray[i:columnlength]]
  j += 1
  i = i + columnlength
  columnlength = columnlength + columnlength
print(columns)
#putting the text back together to form plaintext
plaintextarray = []

i = 0
j = 0
# puts the letters back into original order by getting the nth term in each array and then stringing them together
for i in range (0,columnlength):
  newarray = [columns[j][i]]
  plaintextarray.append(newarray)
  j +=1
  if j == columnnumber - 1:
    j = 0
    i += 1
print(plaintextarray)

plaintext = ''.join(str(x) for x in plaintextarray)

print(plaintext)


from pycipher import ColTrans
import os
import math
import re
import random

loadEnglishNgramDirectory = "/Users/Euan/Desktop/NCC2019/Cryptanalysis/Text_training_data"
loadKeyWordsDirectory = "/Users/Euan/Desktop/NCC2019/Cryptanalysis"


######## ALPHABET LISTS ########
alphabetASCII = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
alphabetCHARACTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#all in expected % occurance
englishLetterFrequency = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]
englishLetterFrequencySorted = [12.702,9.056,8.167,7.507,6.966,6.749,6.327,6.094,5.987,4.253,4.025,2.782,2.758,2.406,2.360,2.228,2.015,1.974,1.929,1.492,0.978,0.772,0.153,0.150,0.095,0.074]
#The above list numbers map to the following letters (in order) -- e t a o i n s h r d l c u m w f g y p b v k j x q z


def loadEnglishNgram(): #loads a ngram file to a python ditionary
        os.chdir(loadEnglishNgramDirectory) #path of ngram file to load make sure .txt file is in this folder MAKE SURE NGRAMS ARE LOWER CASE
        quadramDitionaryEnglish = {}
        with open("ngram.txt", "r") as f:
            for line in f:
                quadramList = line.split()
                quadramDitionaryEnglish[quadramList[0]] = float(quadramList[1])
        return quadramDitionaryEnglish
def loadKeyWords(): #loads a keyword file to a python list
        os.chdir(loadKeyWordsDirectory) #path of ngram file to load make sure .txt file is in this folder MAKE SURE NGRAMS ARE LOWER CASE
        keyWords = []
        with open("keywords.txt", "r") as f:
            for line in f:
                keyWords.append(line.strip("\n"))
        return keyWords
keyWords = loadKeyWords()
ngramDitionaryEnglish = loadEnglishNgram()
def convertToASCII(textList): #Converts an list of characters into an list of their ASCII equivalent numbers
    index = 0
    while index < len(textList): #goes through each list index and turns it from Character to ASCII
        textList[index] = ord(textList[index])
        index += 1
    return textList
def convertToCHARACTER(textList): #Converts an list of ASCII equivalent numbers into an list of their ASCII equivalent characters
    index = 0
    while index < len(textList): #goes through each list index and turns it from ASCII number to Character
        textList[index] = chr(textList[index])
        index += 1
    return textList
def formatString(string): #removes everything apart from a-z lower case from a string
    noPunctuationList = re.findall("[a-z]",string)
    outputString = "".join(noPunctuationList)
    return outputString
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
    final = sum(logAB)
    return final
def randomKey(): #generates a random key
    perms = 0
    key = []
    while perms < 7: #Ensures 26 letters in the alphabet
        randomNo = random.randint(97, 122)
        repeat = search(randomNo,key) #Ensures each letter is unique
        if repeat == False:
            key.append(randomNo)
            perms += 1
    finalKey = "".join(convertToCHARACTER(key))
    return finalKey

t = 0
while t < 5000:
  r = randomKey()
  x = ColTrans(r).decipher("OOHSEERRWCOITUEIEHPIELTINFUTVEOGNRTWDENIIETIGCOATOTIETRCLTLRSESEBHCEOTEOTDONHNETTECNSNCVTAITTUEEUITLAUOTRYDHTLHNURCRITIOAFCMADVSESATIJSTTHNBDOANTTEEEAETHAHILRGEIEEGYNDFTOFREOSKNAHSRLELSTDOODAFLIIIAARNHELBYEEHLHLGHSCTHTBOIUNPTELTRLTESMSIGPTDAEECRAEUDCOLONSEGOFACVALMTBLJNBOHIOAIRNHTMPESRAFABARDGMOEXTESRIGHLSEDERPNGRTEIDEBOIOWRSOILTASRNJRHMTFOTTGNSLHCDSHITRTESLIHNCIWNOPRYEATLSIETEUOYAEEOTGQFNTLSMNEFNRABLWCMUEYHIREEIDEDUTTNNTAOSSNLRNLARBAHNHOERNHDTLOEMDLNNQFIHEECIRFAUARMAPAOEREMEEHSSGSPVRYEDETIIRTEOLYESHSIWCKHNTCOMHSFIOICELEICOADWLOUTCBHEORRATCPELREORPHAFAOETSNFITRSIETYNMIAENTHILAOVTMHHULICAPEIRPELHEOTFAFDOLRSHHYHAREQEHDFPIYTHOISTSOJRMTRUNEBHUHIRLENTLOEILSTICEAYTUNNITNNEAOTNEIGNEISIRLMPAHHSETDCRHNHARTHMWNFRFCSIDIEOIDIEEAVOEROELSEDDHRTTTTSEEHNNSIRIDPNOIIEPUORUEHDETTEOIGUTUYTOODIEEODCHREHHSEAOFMLEHWVSRTRHTSENANIPTVSRISHOEDRELTMTDTOUIDEYERATSERRLNHEGMAEELSETSAIDTLTETDOIHLFPRGAECEOPLHNTAOIEAEMVNPHOSPTIAPLNGSIERTCOEHOPHLTUDLFEKDSCEGEIFARTTLTRUTEPTENAIRCAITEAUHEFSEABIDATTTMUUMIIOTVLPPGYCRTOEOCSAOVRRPAIEIALAAQNEVFNOTRTNRIMFVAGINFRFRMMBNEUUAUTACNDATILMURCRDCOTALGNSAOYRNLHLMETBRDTLRIMFTNTGNTTUTEOEYOHIBWCAEDHEEECNTEUAYIRTONNCIITECLTEHETPTRPUEHMHLNROEYANSEVRDCALSTTUBEUSCTPESGONEHMNCOEIEDLSHWUCLNTAIEEIASITIEUTSGOAFCEESEAEULHVHEFEHHAARONIOFAEORSAOEIIAUNAISTLOTHUITAOTTNUNOPNRSENEIHONJIPYGTPLBEHOEOEOSSTNHXHTCEETRBAIILATYTIDTNMBEUEYFXBPSFLSEEROEIIEASEHYEIOEILADAOFSESETSFRONRNRNTEVUOOEYOISIHMUNEAECSUEOTLEJAEENELEBEGDENDOGSOEKMHRDATRTEYHNEDEHNROVQRRWOMROAACLOHACNHPGIMGUEBSTITCITCRLNTIHIPEUMUSASOEKAAIEMLTNCODSAERNHHNLEURGOAUIRTHGVWBSEARHHOCNLIOSRTOFMHHETETTSLTCEOTCODLIMNEAEHTVYWBSISSSEHHAPLSMIRHEAFASEOTIRIRTTLEAYHTUDREDTTFSIBNOITATSSEODHEPAXLAPFRCVSNIRAEDHROOSMOYPGRMECHWSSEAHTRHCCRRFLEPNMEVEENESAWEEEUESSRDTTHRDOISTMDIEHRNLBUVOOHXEDWESODARNNVOEINOWVASTTIOLOADLTALNHTEUNEETOTPOTSDMRRLTPIETSOWCNDHAANXFIRNSEHUARTTNTRCMNHAWVICTHGCBCIAIUTDVOITSAUKAENCEHDUAPAEEOOFMITCRIILTSERSLIATCIHRDOCEGALTSCINDLAORPTDDHTTOEGESOFGICOIIOVFGMETRISISYIDTARLERRGISEUULCMEETNITLAETUSBTITJMTYOFNSATEEIEAONHSTTELAOTFTNYEHWTOSASOCITTAEAOLPLEOCHLTRICSPNHGUBTOIEODITTIVRIIOORRPEOOMQNBRTSHUSTORRTEIAECLTIOTATEFNRTAEHDNRMUATTUBDIRDTFERSTROEIITSHEDOTREIMTMHEOOHUEIDGTHBMAUCTEIOTHEALOAPAEIESMSLADENKFTPOICPIHREAFCOMHLRLIEFFAYNDURSDAYDLDOAHGPERIRNRSGAISANFDOOEULEGICRRNIOLIILFRARRENIAMAESETNGUNAIOORTOIRSTSFUEOBHARSRIEDANNDDCHLIST")
  y = ngramFitness(x)
  if y > -5000:
    print()
    print(x)
    print()
  t += 1
  '''


from math import log10
import os

class word_score(object):
    def __init__(self):
        ''' load a file containing ngrams and counts, calculate log probabilities '''
        self.Pw = {}
        for line in file('count_1w.txt'):
            key,count = line.split('\t') 
            self.Pw[key.upper()] = self.Pw.get(key.upper(), 0) + int(count)
        self.N = 1024908267229 ## Number of tokens
        #calculate first order log probabilities
        for key in self.Pw.keys():
            self.Pw[key] = log10(float(self.Pw[key])/self.N)
        #get second order word model 
        self.Pw2 = {}
        for line in file('count_2w.txt'):
            key,count = line.split('\t') 
            self.Pw2[key.upper()] = self.Pw2.get(key.upper(), 0) + int(count)
        #calculate second order log probabilities
        for key in self.Pw2.keys():
            word1,word2 = key.split()
            if word1 not in self.Pw: 
                self.Pw2[key] = log10(float(self.Pw2[key])/self.N)
            else: 
                self.Pw2[key] = log10(float(self.Pw2[key])/self.N) - self.Pw[word1]
        # precalculate the probabilities we assign to words not in our dict, L is length of word
        self.unseen = [log10(10./(self.N * 10**L)) for L in range(50)]        
        
    # conditional word probability    
    def cPw(self,word,prev='<UNK>'):
        if word not in self.Pw: 
            return self.unseen[len(word)]
        elif prev+' '+word not in self.Pw2: 
            return self.Pw[word]
        else: 
            return self.Pw2[prev+' '+word]
    
    def score(self,text,maxwordlen=20):
        prob = [[-99e99]*maxwordlen for _ in range(len(text))]
        strs = [['']*maxwordlen for _ in range(len(text))]
        for j in range(maxwordlen):
            prob[0][j] = self.cPw(text[:j+1])
            strs[0][j] = [text[:j+1]]
        for i in range(1,len(text)):
            for j in range(maxwordlen):
                if i+j+1 > len(text): break
                candidates = [(prob[i-k-1][k] + self.cPw(text[i:i+j+1],strs[i-k-1][k][-1]),
                               strs[i-k-1][k] + [text[i:i+j+1]] ) for k in range(min(i,maxwordlen))]
                prob[i][j], strs[i][j] = max(candidates)
        ends = [(prob[-i-1][i],strs[-i-1][i]) for i in range(min(len(text),maxwordlen))]
        return max(ends)





fitness = word_score()
x = fitness.score('HELLOHOWAREYOUTODAY')
print(x)




cipher="OOHSEERRWCOITUEIEHPIELTINFUTVEOGNRTWDENIIETIGCOATOTIETRCLTLRSESEBHCEOTEOTDONHNETTECNSNCVTAITTUEEUITLAUOTRYDHTLHNURCRITIOAFCMADVSESATIJSTTHNBDOANTTEEEAETHAHILRGEIEEGYNDFTOFREOSKNAHSRLELSTDOODAFLIIIAARNHELBYEEHLHLGHSCTHTBOIUNPTELTRLTESMSIGPTDAEECRAEUDCOLONSEGOFACVALMTBLJNBOHIOAIRNHTMPESRAFABARDGMOEXTESRIGHLSEDERPNGRTEIDEBOIOWRSOILTASRNJRHMTFOTTGNSLHCDSHITRTESLIHNCIWNOPRYEATLSIETEUOYAEEOTGQFNTLSMNEFNRABLWCMUEYHIREEIDEDUTTNNTAOSSNLRNLARBAHNHOERNHDTLOEMDLNNQFIHEECIRFAUARMAPAOEREMEEHSSGSPVRYEDETIIRTEOLYESHSIWCKHNTCOMHSFIOICELEICOADWLOUTCBHEORRATCPELREORPHAFAOETSNFITRSIETYNMIAENTHILAOVTMHHULICAPEIRPELHEOTFAFDOLRSHHYHAREQEHDFPIYTHOISTSOJRMTRUNEBHUHIRLENTLOEILSTICEAYTUNNITNNEAOTNEIGNEISIRLMPAHHSETDCRHNHARTHMWNFRFCSIDIEOIDIEEAVOEROELSEDDHRTTTTSEEHNNSIRIDPNOIIEPUORUEHDETTEOIGUTUYTOODIEEODCHREHHSEAOFMLEHWVSRTRHTSENANIPTVSRISHOEDRELTMTDTOUIDEYERATSERRLNHEGMAEELSETSAIDTLTETDOIHLFPRGAECEOPLHNTAOIEAEMVNPHOSPTIAPLNGSIERTCOEHOPHLTUDLFEKDSCEGEIFARTTLTRUTEPTENAIRCAITEAUHEFSEABIDATTTMUUMIIOTVLPPGYCRTOEOCSAOVRRPAIEIALAAQNEVFNOTRTNRIMFVAGINFRFRMMBNEUUAUTACNDATILMURCRDCOTALGNSAOYRNLHLMETBRDTLRIMFTNTGNTTUTEOEYOHIBWCAEDHEEECNTEUAYIRTONNCIITECLTEHETPTRPUEHMHLNROEYANSEVRDCALSTTUBEUSCTPESGONEHMNCOEIEDLSHWUCLNTAIEEIASITIEUTSGOAFCEESEAEULHVHEFEHHAARONIOFAEORSAOEIIAUNAISTLOTHUITAOTTNUNOPNRSENEIHONJIPYGTPLBEHOEOEOSSTNHXHTCEETRBAIILATYTIDTNMBEUEYFXBPSFLSEEROEIIEASEHYEIOEILADAOFSESETSFRONRNRNTEVUOOEYOISIHMUNEAECSUEOTLEJAEENELEBEGDENDOGSOEKMHRDATRTEYHNEDEHNROVQRRWOMROAACLOHACNHPGIMGUEBSTITCITCRLNTIHIPEUMUSASOEKAAIEMLTNCODSAERNHHNLEURGOAUIRTHGVWBSEARHHOCNLIOSRTOFMHHETETTSLTCEOTCODLIMNEAEHTVYWBSISSSEHHAPLSMIRHEAFASEOTIRIRTTLEAYHTUDREDTTFSIBNOITATSSEODHEPAXLAPFRCVSNIRAEDHROOSMOYPGRMECHWSSEAHTRHCCRRFLEPNMEVEENESAWEEEUESSRDTTHRDOISTMDIEHRNLBUVOOHXEDWESODARNNVOEINOWVASTTIOLOADLTALNHTEUNEETOTPOTSDMRRLTPIETSOWCNDHAANXFIRNSEHUARTTNTRCMNHAWVICTHGCBCIAIUTDVOITSAUKAENCEHDUAPAEEOOFMITCRIILTSERSLIATCIHRDOCEGALTSCINDLAORPTDDHTTOEGESOFGICOIIOVFGMETRISISYIDTARLERRGISEUULCMEETNITLAETUSBTITJMTYOFNSATEEIEAONHSTTELAOTFTNYEHWTOSASOCITTAEAOLPLEOCHLTRICSPNHGUBTOIEODITTIVRIIOORRPEOOMQNBRTSHUSTORRTEIAECLTIOTATEFNRTAEHDNRMUATTUBDIRDTFERSTROEIITSHEDOTREIMTMHEOOHUEIDGTHBMAUCTEIOTHEALOAPAEIESMSLADENKFTPOICPIHREAFCOMHLRLIEFFAYNDURSDAYDLDOAHGPERIRNRSGAISANFDOOEULEGICRRNIOLIILFRARRENIAMAESETNGUNAIOORTOIRSTSFUEOBHARSRIEDANNDDCHLIST"



def transposition(userCipherText):
    keyLength = 7
    charCount = 2303
    colLen = charCount / keyLength
    cipher = list(userCipherText)
    perms = 0
    index = 0
    itera = 1
    arrayL = []
    while perms < keyLength:
        array = []
        while index < ((colLen*itera)):
            new = cipher[index]
            array.append(new)
            index+=1
        arrayL.append(array)
        perms+=1
        itera+=1
    return arrayL

def solve(array):
    arrayN=[]
    keyLength = 7
    charCount = 2303
    colLen = charCount / keyLength
    index = 0
    while index < colLen:
        perms=0
        while perms < keyLength:
            new = array[index][perms]
            arrayN.append(new)
            perms+=1
        if index == 6:
            index = 0
        else:
            index+=1
    x = "".join(arrayN)
    return x
    #nn = ngramFitness(x)

    
def addPadding(cipher,Key): # pads a transposition ciphertext with a padding character of X
    cipher = list(cipher)
    lengthCipher = len(cipher)
    remainder = lengthCipher % key # Finds how many padding characters to add
    if remainder == 0: #If the ciphertext length is divisible by the key perfectly then no padding is needed
        return "".join(cipher)
    else:
        addPad = 0
        while addPad < remainder: # Loops round the cipher text array adding a padding character each time
            cipher.append("x") # The padding character
            addPad+=1
        return "".join(cipher)
    
    
    
    
x = transposition(cipher)
y = solve(x)
print(y)
print(x)
