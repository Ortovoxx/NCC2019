#==============================================================================================================================================================
#                                                                          Euan Caskie 
#
#                                                                   National Cipher Challenge
#
#
#                                                             IMPORTANT INFO BEFORE USING THIS PROGRAM:
#
#==============================================================================================================================================================

# Change this so it navigates to the directory with the github "NCC2019" folder in -- Automatically in the C drive
toNCC2019 = "/Users/Euan/Desktop"

# Leave these the same provided you just cloned from github
loadEnglishNgramDirectory = toNCC2019 + "/NCC2019/Cryptanalysis/Text_training_data"
loadKeyWordsDirectory = toNCC2019 + "/NCC2019/Cryptanalysis"
outputFilesHere = toNCC2019 + "/NCC2019/Out"
wordScoreDir = toNCC2019 + "/NCC2019/Cryptanalysis/word counts"
# All functions should transfer data using lowercase no space no punctuation strings

#########  TEST CIPHERS TO TRY AND SOLVE  #########
userCipherNoFormatBypass = "rborpktigovcrbbwucjawjklojhcjdkmsktpqocqrbwrloklgovcggcjqcqrkjskhcjawgkjawjdrpycjarkltrrbcjaqcjcr"
userCipherNoFormatBypass = "TjfBsppxrippxrssqjubijvpdhjespojwreybszrhmdhsrwpsrsbpenbaqjwraaibjyspsqjsjksRsubwhsbszrhqrwysphrvbusqrszrhrcdfpwrujrsdwjreyepwtriivBzpdiyrhhdtjcdfcdsbshjjtjypyysqrsbszrhsqjpeivubijsqrszrhruujnsjyhpBrhxjyrwpdeysphjjburevpejqryhjjerevsqbefhbtbirw.Bssdwehpdssqrssqbhzrhepssqjubwhserobfrsbpeawpcijtspqbssqjawpfwrttj.FjejwjapwsjyrtrmpwbhhdjzbsqsqjfdbyrenjawpfwrttjupwHeppavpesqjRapiipSjetbhhbpezqbnqnpdiyrfrbeqrojnrdhjyrtrmpwawpcijt.Upwhptjwjrhpesqjawpfwrttjnpeswpiibefsqjireybefwryrwzrhe’sdayrsjyzbsqsqjuibfqsairereybuFjejqrye’swrbhjysqrszbsqBojwhpesqjesqjcpvhtbfqsqrojqrywjriswpdcijfjssbefcrnx.Bippxjysqwpdfqsqjnptarevubijhreyupdeyrepsqjwpupdwtvhsjwbpdhivupwtrssjywjapwsh:sqjtjtpbeupwtbefsqjtrcpdssqjnqrefj,zqbnqjkairbehzqvsqjawpfwrttjejojwfpsdayrsjy.Sqbhsbtjsqjnbaqjwzrhreruubejhqbus,hphibfqsivqrwyjwspnwrnx,cdsepsqbefhjwbpdh.Hsbii,bsbhtdnqijhhibxjivsqrsbszrhrcdfsqrssbtj,reyberevnrhjszbnjbhspptdnqpurnpbenbyjenj.Bsybyhsrwstjzpeyjwbefzqvsqjhjnpeynbaqjwzrhjrhbjwspnwrnxsqresqjubwhs,cdssqjeBwjribhjysqrssqjruubejhqbuszrhspptdnqpurfbojrzrv.Rwpsrsbpenbaqjwwjriivnpdiymdhscjrejenpybefjwwpw,cdssqjruubejhqbusbhspphpaqbhsbnrsjyupwrtbhsrxj,hpzqpjojwtrefijysqjwjapwshtdhsqrojwjribhjysqjvqrytryjrcbspurejwwpwzbsqsqjubwhspejreyswbjyspnpojwsqjbwhsjahzbsqsqjhjnpey.Bsbhqrwysphjjsqbhrhrevsqbefpsqjwsqrerssjtasjyhrcpsrfj,cdsBrtepshdwjzqrssqjtpsbojnpdiycj.Bypdcsbsbhajwhperi.SqjRapiipSjereyJijojenwjzhype’spojwira,hpjbsqjwhptjpejqrhrfwdyfjrfrbehssqjzqpijRhswperdsnpwahpwsqjvrwjswvbefspyjwrbisqjRapiipawpfwrttj.BsnpdiycjsqjHpobjshBhdaaphj.Rsubwhs,BsqpdfqssqrssqjbwzbiibefejhhsphqbussqjIDER-UBUSJJEpwcbshqpzjysqrssqjvzjwje’sarwspubs,cdshptjpejbesqjHsrsjYjarwstjesapbesjypdssqrssqjvtbfqsmdhsqrojqryrfdbisvnpehnbjenj,pwcjjexjjespybhsrenjsqjthjiojhpenjsqjaipszrhybhnpojwjy.Brthsbiiepshdwj.Besqjtjresbtj,npdiyvpdsrxjrippxrssqjnptadsjwubijhsphjjzqptbfqsqrojqryrnnjhhspcpsqtjtph,reyzqptbfqsqrojqrysqjpaapwsdebsvreytjrehspypnspwsqjt?BrtuivbefcrnxspIrefijvspebfqssphjjbusqjHsrsjYjarwstjesqrojrevbyjrhzqrstbfqscjfpbefpeEjbihrbyqjnpdiyuivtjdabepejpusqjERHRnqrhjairejhzqbnqbhhptjsqbefBqrojcjjexjjespswv.BzbiinriivpdbuBfjsrevsqbef"
userCipherNoFormatBypass = "xqhhoyqcdejikhuyvoekmuhusefyutydjejxucuceqrekjhusudjuludjirkjxuhuyiqikccqhojmetqoiqweqdevvtkjowkytqdsuevvysuhqbuhjutcyiiyedsedjhebjeqfejudjyqbfherbucmyjxjxuqfebbevbywxjjxufbqdduttuisudjjhqzusjehoqffuqhutjeruhkddydwedqsebbyiyedsekhiumyjx"
userCipherNoFormatBypass = "WKMPCZKXDVSYEZUKYLTVICYFKBVDDNKZKXDVMYXOBPKLPXMDNKCDVLLVXTDBIPXMDYMVEMKDNKWYYTDNKBKIYEVBKBPMNDDNKNVGRCVBKMKDDPXMZBKDDIBKCDUKCCVXTNVFKWYBKYBUKCCTKSPTKTVUBKVTIDNVDDNKCYFPKDCVBKDYOUVWKLYBBKSKXDKFKXDCYXDNKVZYUUYZBYMBVWWKCYWKYLDNKMKXKBVUCTYXDXKKTWESNYLVXKHSECKDYDEBXEZDNKNKVDOEDIYETYXDMKDLYEBCDVBCGPDNYEDEXTKBCDVXTPXMDNKXKKTLYBZYUPDPSVUCEZZYBDVXTDNKBKNVCOKKXVSYXSKBDKTGNPCZKBPXMSVWZVPMXDYSYXFPXSKDNKZBKCPTKXDDYDVRKVCDBYXMUPXKDNKWYCDCDBPTKXDVBKSVUUPXMLYBVUVBMKOEPUTEZYLLYBSKCVUYXMDNKOYBTKBGPDNKVCDMKBWVXIVCVCNYGYLCDBKXMDNVBMEPXMDNVDDNKVDDVSRYXDNKCZVSKZBYMBVWWKWECDNVFKOKKXVEDNYBPCKTOIDNKZYUPDOEBYDNVDWVRKCXYCKXCKDYWKLPBCDDNKBECCPVXCVBKWYBKUPRKUIDYDBIDYGPXDNKZBYZVMVXTVGVBDNVXDYBPCRSYXLUPSDVXTCKSYXTDNKCVOYDVMKPLDNVDPCGNVDPDPCPCXDCYZNPCDPSVDKTKXYEMNLYBVRMOYZKBVDPYXOEDPDPCNVBTDYSYXFPXSKDNKMKXKBVUCDNVDDNVDPCDBEKCYWKYLDNKWYBKSVEDPYECZUVXXKBCWYCDUIDNYCKGNYVSDEVUUILYEMNDPXDNKUVCDGVBNVFKWVXVMKTDYOUYSRDNKOEPUTEZZBYZYCPXMVXKGDBVXSNKYLGVBMVWKCPXCDKVTWYOPUPCPXMDNVDGVIPCCDPUUVZBYFYSVDPYXOEDPCUKCCUPRKUIDYVSSPTKXDVUUIDBPMMKBVGVBKCZKSPVUUIPLGKXYDPLIZVFUYFCRIPXVTFVXSKVUUDNKCVWKWIYGXDPWKPXOKBUPXSYXFPXSKTWKGKNVFKDYDBKVTFKBICYLDUIDNKBKCYPNKVTKTYFKBDYUVXMUKIVXTSYXFPXSKTDNKWDYCEMMKCDVXVUDKBXVDPFKGKGPUUCDKZEZPXCZKSDPYXCVDSNKSRZYPXDSNVBUPKDYWVRKPDNVBTKBLYBCYFPKDVMKXDCDYSBYCCVXTSBVXREZDNKDKELKUCOKBMUPCDKXPXMYZKBVDPYXDYCKKPLDNVDDEBXCEZVXIDNPXMBKUVDKTPVWVUCYMYPXMDYCKXTVSYEZUKYLYEBOKCDYFKBDYOVPRYXEBDYDBIVXTLPXTYEDGNVDPCMYPXMYXDNKBKDNKCYFPKDCVBKZBKDDICKSBKDPFKVOYEDDNKPBYGXCZVSKZBYMBVWWKVXTGPDNYEDDNKGYBUTCZBKCCGVDSNPXMGKTYXDBKVUUINVFKVSUKVBZPSDEBKYLDNKPBZBYMBKCCYBDNKPBZUVXCEXUKCCDNKIVBKSUYCKDYZEDDPXMDNKPBYGXWKXYXDNKWYYXPSVXDCKKGNVDDNKINVFKDYMVPXGPDNGNVDCKKWCDYOKVLVPBUITPCYBMVXPCKTVDDKWZDDYTKBVPUYEBCZVSKZBYMBVWWKOEDPGYEUTCDPUUUPRKDYRXYGGNVDDNKIVBKEZDYRKKZVSUYCKKIKYXDNKWPCCPYXZUVXXPXMVXTUKDWKRXYGPLIYENKVBVXIDNPXMGYBBIPXMPGPUUOKOVSRVOYEDVGKKROKLYBKDNKUVEXSNNVBBI"
userCipherNoFormatBypass = "pmpafxaikkitprdsikcplifhwceigixkirradfeirdgkipgigudkcekiigpwrpucikceiginasikwduearrxiiqepcceindgmieinpwdfprduppcedoikiqiasafmfddfipfgmdafmfdteiki"

#==============================================================================================================================================================
#                                                                  VARIABLES, CONSTANTS AND FORMATTING - DO NOT EDIT
#==============================================================================================================================================================

#Modules to imports
import random
import os
import math
from math import log10
import time
import re
import json
import sys

#Custom modules to import
import textManipulation as tx

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

clear = lambda: os.system("cls") #Clears the console

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
keyWords = loadKeyWords() #Calls the above functions to load them into memory from a file - Comment out if you dont need them and want to go faster
ngramDitionaryEnglish = loadEnglishNgram()

#==============================================================================================================================================================
#                                                       TEXT MANIPULATION AND REPEATED USE FUNCTIONS - DO NOT EDIT
#==============================================================================================================================================================

class wordScore(object):
    os.chdir(wordScoreDir)
    def __init__(self):
        ''' load a file containing ngrams and counts, calculate log probabilities '''
        self.Pw = {}
        with open('1word_counts.txt', "r") as f:
            lines  = f.readlines()
            for line in lines:
                key,count = line.split('\t') 
                self.Pw[key.upper()] = self.Pw.get(key.upper(), 0) + int(count)
        self.N = 1024908267229 ## Number of tokens
        #calculate first order log probabilities
        for key in self.Pw.keys():
            self.Pw[key] = log10(float(self.Pw[key])/self.N)
        #get second order word model 
        self.Pw2 = {}
        with open('2word_counts.txt', "r") as f:
            lines = f.readlines()
            for line in lines:
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
    
    def words(self,text,maxwordlen=20):
        text = "".join(re.findall("[a-z]",text.lower())).upper()
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
        return " ".join(max(ends)[1]).lower()
defrag = wordScore()

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
    textList = tx.convertToASCII(list(text))
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
    textList = tx.convertToASCII(list(text))
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

#==============================================================================================================================================================
#                                                            CIPHER SOLVING - EDITABLE
#==============================================================================================================================================================

def addPadding(cipher,key): # pads a transposition ciphertext with a padding character of X
    cipher = list(cipher)
    lengthCipher = len(cipher)
    remainder = lengthCipher % key # Finds how many padding characters to add
    if remainder == 0: #If the ciphertext length is divisible by the key perfectly then no padding is needed
        return "".join(cipher)
    else:
        addPad = 0
        while addPad <= remainder: # Loops round the cipher text array adding a padding character each time
            cipher.append("x") #~~~~ The padding character ~~~~#
            addPad+=1
        return "".join(cipher)

def textBlock(textIn,blockSize): #Takes a plaintext string input and returns a list with a sublist of blocked characters
    text = list(textIn)
    length = len(text)
    blockedText = []
    remainder = length % blockSize
    index = addPad = 0
    if remainder != 0:
        while addPad <= remainder: # Loops round the cipher text array adding a padding character each time
            text.append("x") # The padding character
            addPad += 1
    while index < length:
        blocked = []
        blocking = 0
        while blocking < blockSize:
            add = text[blocking + index]
            blocked.append(add)
            blocking += 1
        blockedText.append("".join(blocked))
        index += blockSize
    return blockedText

def textReplace(textBlockIN,find,replace):#Takes an array with strings of blocked characters and repalces them with others
    textBlockOUT = []
    for n in textBlockIN:
        new = n.replace(find,replace)
        textBlockOUT.append(new)
    return textBlockOUT

def factors(textIn): # Finds the factors of the length of a ciphertext
    length = len(list(textIn))
    factorList = [length]
    for i in range(1,length):
        if length % i == 0:
            factorList.append(int(i))
    return sorted(factorList)

#==============================================================================================================================================================
#                                                               TRANSPOSITION SOLVERS
#==============================================================================================================================================================

def readInVertical(userCipherText,keyLength): # Transposes a ciphertext into a list of *keyLength* columns of equal length writes abcdef as a colum of abc then another colum of def. Vertical
    columnLength = len(userCipherText) / keyLength # Finds how long each column needs to be << Should be integer if float then there will be unequal columns... padding needed
    cipher = list(userCipherText) 
    noColumns = index = 0
    cipherShiftValue = 1
    transposed = []
    while noColumns < keyLength: # Iterates through entire ciphertext
        column = []
        while index < (columnLength * cipherShiftValue): # Iterates through each individual column and * by cipherShiftValue to ensure the previous letters are not counted
            column.append(cipher[index])
            index += 1
        transposed.append(column)
        noColumns += 1
        cipherShiftValue += 1
    return transposed # List with lists inside. Effectively just split up the ciphertext into *keylength* equal parts

def readInHorizontal(userCipherText,keyLength): # Transposes a ciphertext into a list of *keyLength* columns of equal length writes abcdef as a row of abc then another row of def. Horizontal
    columnLength = len(userCipherText) / keyLength # Finds how long each column needs to be << Should be integer if float then there will be unequal columns... padding needed
    cipher = list(userCipherText) 
    noRows = index = 0
    cipherShiftValue = 1
    transposed = []
    while noRows < columnLength: # Iterates through entire ciphertext
        row = []
        while index < (keyLength * cipherShiftValue): # Iterates through each individual row and * by cipherShiftValue to ensure the previous letters are not counted
            row.append(cipher[index])
            index += 1
        transposed.append(row)
        noRows += 1
        cipherShiftValue += 1
    return transposed

userCipher = "OOHSEERRWCOITUEIEHPIELTINFUTVEOGNRTWDENIIETIGCOATOTIETRCLTLRSESEBHCEOTEOTDONHNETTECNSNCVTAITTUEEUITLAUOTRYDHTLHNURCRITIOAFCMADVSESATIJSTTHNBDOANTTEEEAETHAHILRGEIEEGYNDFTOFREOSKNAHSRLELSTDOODAFLIIIAARNHELBYEEHLHLGHSCTHTBOIUNPTELTRLTESMSIGPTDAEECRAEUDCOLONSEGOFACVALMTBLJNBOHIOAIRNHTMPESRAFABARDGMOEXTESRIGHLSEDERPNGRTEIDEBOIOWRSOILTASRNJRHMTFOTTGNSLHCDSHITRTESLIHNCIWNOPRYEATLSIETEUOYAEEOTGQFNTLSMNEFNRABLWCMUEYHIREEIDEDUTTNNTAOSSNLRNLARBAHNHOERNHDTLOEMDLNNQFIHEECIRFAUARMAPAOEREMEEHSSGSPVRYEDETIIRTEOLYESHSIWCKHNTCOMHSFIOICELEICOADWLOUTCBHEORRATCPELREORPHAFAOETSNFITRSIETYNMIAENTHILAOVTMHHULICAPEIRPELHEOTFAFDOLRSHHYHAREQEHDFPIYTHOISTSOJRMTRUNEBHUHIRLENTLOEILSTICEAYTUNNITNNEAOTNEIGNEISIRLMPAHHSETDCRHNHARTHMWNFRFCSIDIEOIDIEEAVOEROELSEDDHRTTTTSEEHNNSIRIDPNOIIEPUORUEHDETTEOIGUTUYTOODIEEODCHREHHSEAOFMLEHWVSRTRHTSENANIPTVSRISHOEDRELTMTDTOUIDEYERATSERRLNHEGMAEELSETSAIDTLTETDOIHLFPRGAECEOPLHNTAOIEAEMVNPHOSPTIAPLNGSIERTCOEHOPHLTUDLFEKDSCEGEIFARTTLTRUTEPTENAIRCAITEAUHEFSEABIDATTTMUUMIIOTVLPPGYCRTOEOCSAOVRRPAIEIALAAQNEVFNOTRTNRIMFVAGINFRFRMMBNEUUAUTACNDATILMURCRDCOTALGNSAOYRNLHLMETBRDTLRIMFTNTGNTTUTEOEYOHIBWCAEDHEEECNTEUAYIRTONNCIITECLTEHETPTRPUEHMHLNROEYANSEVRDCALSTTUBEUSCTPESGONEHMNCOEIEDLSHWUCLNTAIEEIASITIEUTSGOAFCEESEAEULHVHEFEHHAARONIOFAEORSAOEIIAUNAISTLOTHUITAOTTNUNOPNRSENEIHONJIPYGTPLBEHOEOEOSSTNHXHTCEETRBAIILATYTIDTNMBEUEYFXBPSFLSEEROEIIEASEHYEIOEILADAOFSESETSFRONRNRNTEVUOOEYOISIHMUNEAECSUEOTLEJAEENELEBEGDENDOGSOEKMHRDATRTEYHNEDEHNROVQRRWOMROAACLOHACNHPGIMGUEBSTITCITCRLNTIHIPEUMUSASOEKAAIEMLTNCODSAERNHHNLEURGOAUIRTHGVWBSEARHHOCNLIOSRTOFMHHETETTSLTCEOTCODLIMNEAEHTVYWBSISSSEHHAPLSMIRHEAFASEOTIRIRTTLEAYHTUDREDTTFSIBNOITATSSEODHEPAXLAPFRCVSNIRAEDHROOSMOYPGRMECHWSSEAHTRHCCRRFLEPNMEVEENESAWEEEUESSRDTTHRDOISTMDIEHRNLBUVOOHXEDWESODARNNVOEINOWVASTTIOLOADLTALNHTEUNEETOTPOTSDMRRLTPIETSOWCNDHAANXFIRNSEHUARTTNTRCMNHAWVICTHGCBCIAIUTDVOITSAUKAENCEHDUAPAEEOOFMITCRIILTSERSLIATCIHRDOCEGALTSCINDLAORPTDDHTTOEGESOFGICOIIOVFGMETRISISYIDTARLERRGISEUULCMEETNITLAETUSBTITJMTYOFNSATEEIEAONHSTTELAOTFTNYEHWTOSASOCITTAEAOLPLEOCHLTRICSPNHGUBTOIEODITTIVRIIOORRPEOOMQNBRTSHUSTORRTEIAECLTIOTATEFNRTAEHDNRMUATTUBDIRDTFERSTROEIITSHEDOTREIMTMHEOOHUEIDGTHBMAUCTEIOTHEALOAPAEIESMSLADENKFTPOICPIHREAFCOMHLRLIEFFAYNDURSDAYDLDOAHGPERIRNRSGAISANFDOOEULEGICRRNIOLIILFRARRENIAMAESETNGUNAIOORTOIRSTSFUEOBHARSRIEDANNDDCHLIST"
userCipher = "WWWESWWEHRASWRASIITAIITXCSCRSSCXHTHESTHX"

x = readInVertical(userCipher,5)

'''
for i in x:
    print(i)
input("")
'''
def readOffVertical(userCipherArray):
    index = 0
    output = []
    while index < len(userCipherArray[0]):
        for row in userCipherArray:
            output.append(row[index])
        index += 1
    return "".join(output)



#ORELVWTOLEENSTTYUOVJDEHETKEDABLTTETAOABITFMRDTILRTDEIETETNMETSAOLNCRRSETHNFELEPPTSILHEEOHDORBELYNEIHHMSDEDTSORTUEEFSEVETEEGELHENESNCLKITEIFAMPOVIETARUDRAYERGOWEANLTHACBEMDLIUCUENRALAOEPESTATEPRSEFFNEMSJEDMTERACGTNUELALUWHSHLOABHISRHTOEXVDOCHREASRDBEAITDTOMEDIACICVKDORRIGNTEIFSAIMLTOESTWCOHPOTOMHTTFDTTOEMHHELEEIARYAHNAURLNEIROIDOWITEDITTBOENTLDRASSOEIEONLAAYGBESDENCLOMAOIEEOTHGSSWAEOLRUETSREOQIMEGDESTIIOOEHSIAAUIOLAFIMHNSTNIRSNWIIRDSIIUEYEHMRNSDDYRMTTLCTMPGOTDFRNTSTIPERAVNGMAACLRTINECEYCTRLNAESNLNATELHISUOOPIYHSCIIUSOEISRTYUUABOHEHRANUCTMKTEEIBORETDESHRETTTIOLSHYHTFVWSDIUDRNTLETRTHRRMCIOAUOISHADDGCGIRSEAIFITFTILLNIIRQUEINNUFEDTUBIOSNCFLNYGRNLNFITOSBECHCEIOEGILHTTCUAHCFETAALGFASFREHOLMAUSVJAPBEGRIWAMNHLNTUTSAEINNBREFRAMSEOICOCURLANEEOLRTRRPSTUTTUEGLEHNDEOHERIEOTOHLTARRTERASEFEAVTSEUSAUAEETIGORLFRIMUTRGNBMTYACIIEPNSLUGCSTSSEHHOANTTNHGOTEIDEFEHLEOEONEEEGRYNWCHEIIUANRURSCTTCLHIAHOTUFTDANRPWRLEEROEVWNOITUPRSANTNTAIEAFILRLLDEOMSLEEETNETTOTPTHEVRNSIORRBEIOMEMOAMKPCIDDPSFEIRANOTHDHSOHNGNCERCDTVEUTRCSTNERYRHTLNESITSEDEANIEAXHPDRSTSIIOLOGMBYDNLANMIFPEPTLWOIOTRRFFTNVIPFSEITRHLINANMTAFIEEREIEHIODSERNIEORLEATPOONIIHDCRTIAATOYCPANINBTIDNLRFTOENRIHURESSOOHAIGSVAFOAHTROTENELTYLIYASNVIEOEGSDHROLPBTHSACNRTENOEEITSPETLDSAHPIOGSHEEEDIHOENWOANOLOASTHHITNPMLIDTAHSIEYEUTTJSAENSTLRGORPBTATTMDRITHIATPSFIOEULEGDGOAMGRSAALEIPFNIOTSEOETEOLIMAHTTGNESDIHHCURIECGLBRSRTLNESRFLTHPSYQNLHETRHHDHAAEVIYCMCACAEAIYTTCEAHQYSUIOCNOEPDRREALTHDPDGOCEHHISLUANEIDRPIPAEOLETERUBMTCSAAOMFNALCSHDTUHDTTTEEOVTCNEWITOEHAAEIUNSNPOHTANFSIEDERUSATNDOANOMOGSCIAIOHGHALFTOMVSLAIERITEFRORSCPNETSROSVVLLETTWNENAGUSCAITAOSOTOITIRUNUMAOLYAAEIUDIEROEAAUISTREDUHALTHMFRDRAOILRAUTFRNIETIURIAREONCAUTHTATNTHEDOROIELTNLGCOOMONRDESGBONOHRNRIAFEWIDANNDLEUOHRIEKHEDBTOOTNHMALFHETONREEITIACTFOVSTNPUEUDHAWTPHTITHLDOGLEHPRPFGTPCHIUVRAIQTFRECMOALTNTIHEOETHERTTEIUEIAAEREISIUEJLEXRTMXEEIATNOIELEEETEVRHITRPSEDHOGRIMTTNYSSFRAEBSPRASMECNEUTTNHOOAONESPCXHTWCTAEETSTCCRTFORDRLISTTNAESEOCBIIOTRCTEARTSEOGCEEAPRHFSOIIOCIRENOUSNSRUETTETCSTHNIIRNIDIBEAIFSLOILHHPTPRLFTHHAGSEROIJTCTCYEENFCRUOLHTNEAESYRSHSLWHCRERMIHPHDYHHJELIATNSHRHCIOETNNOTTIROVSTOMDSESTIAHAOLTHEELTAEDULTOENRVFUNUTOMLTEBEUNCPMYDUPHECEEFEFOOITTNNIBOHBYBBEAOOSROHCELNKRDQOAMILEOMSNAVHOHSCEWEMAIYDNSACEMEARMSEHMLXDESAHTDINFURVBDUHECECEIPOGVITGCTBYEHOHOACSTTOOSRLEHTDRHIOTTAIDOELADARSERIESAIERDT
#ORELVWTOLEENSTTYUOVJDEHETKEDABLTTETAOABITFMRDTILRTDEIETETNMETSAOLNCRRSETHNFELEPPTSILHEEOHDORBELYNEIHHMSDEDTSORTUEEFSEVETEEGELHENESNCLKITEIFAMPOVIETARUDRAYERGOWEANLTHACBEMDLIUCUENRALAOEPESTATEPRSEFFNEMSJEDMTERACGTNUELALUWHSHLOABHISRHTOEXVDOCHREASRDBEAITDTOMEDIACICVKDORRIGNTEIFSAIMLTOESTWCOHPOTOMHTTFDTTOEMHHELEEIARYAHNAURLNEIROIDOWITEDITTBOENTLDRASSOEIEONLAAYGBESDENCLOMAOIEEOTHGSSWAEOLRUETSREOQIMEGDESTIIOOEHSIAAUIOLAFIMHNSTNIRSNWIIRDSIIUEYEHMRNSDDYRMTTLCTMPGOTDFRNTSTIPERAVNGMAACLRTINECEYCTRLNAESNLNATELHISUOOPIYHSCIIUSOEISRTYUUABOHEHRANUCTMKTEEIBORETDESHRETTTIOLSHYHTFVWSDIUDRNTLETRTHRRMCIOAUOISHADDGCGIRSEAIFITFTILLNIIRQUEINNUFEDTUBIOSNCFLNYGRNLNFITOSBECHCEIOEGILHTTCUAHCFETAALGFASFREHOLMAUSVJAPBEGRIWAMNHLNTUTSAEINNBREFRAMSEOICOCURLANEEOLRTRRPSTUTTUEGLEHNDEOHERIEOTOHLTARRTERASEFEAVTSEUSAUAEETIGORLFRIMUTRGNBMTYACIIEPNSLUGCSTSSEHHOANTTNHGOTEIDEFEHLEOEONEEEGRYNWCHEIIUANRURSCTTCLHIAHOTUFTDANRPWRLEEROEVWNOITUPRSANTNTAIEAFILRLLDEOMSLEEETNETTOTPTHEVRNSIORRBEIOMEMOAMKPCIDDPSFEIRANOTHDHSOHNGNCERCDTVEUTRCSTNERYRHTLNESITSEDEANIEAXHPDRSTSIIOLOGMBYDNLANMIFPEPTLWOIOTRRFFTNVIPFSEITRHLINANMTAFIEEREIEHIODSERNIEORLEATPOONIIHDCRTIAATOYCPANINBTIDNLRFTOENRIHURESSOOHAIGSVAFOAHTROTENELTYLIYASNVIEOEGSDHROLPBTHSACNRTENOEEITSPETLDSAHPIOGSHEEEDIHOENWOANOLOASTHHITNPMLIDTAHSIEYEUTTJSAENSTLRGORPBTATTMDRITHIATPSFIOEULEGDGOAMGRSAALEIPFNIOTSEOETEOLIMAHTTGNESDIHHCURIECGLBRSRTLNESRFLTHPSYQNLHETRHHDHAAEVIYCMCACAEAIYTTCEAHQYSUIOCNOEPDRREALTHDPDGOCEHHISLUANEIDRPIPAEOLETERUBMTCSAAOMFNALCSHDTUHDTTTEEOVTCNEWITOEHAAEIUNSNPOHTANFSIEDERUSATNDOANOMOGSCIAIOHGHALFTOMVSLAIERITEFRORSCPNETSROSVVLLETTWNENAGUSCAITAOSOTOITIRUNUMAOLYAAEIUDIEROEAAUISTREDUHALTHMFRDRAOILRAUTFRNIETIURIAREONCAUTHTATNTHEDOROIELTNLGCOOMONRDESGBONOHRNRIAFEWIDANNDLEUOHRIEKHEDBTOOTNHMALFHETONREEITIACTFOVSTNPUEUDHAWTPHTITHLDOGLEHPRPFGTPCHIUVRAIQTFRECMOALTNTIHEOETHERTTEIUEIAAEREISIUEJLEXRTMXEEIATNOIELEEETEVRHITRPSEDHOGRIMTTNYSSFRAEBSPRASMECNEUTTNHOOAONESPCXHTWCTAEETSTCCRTFORDRLISTTNAESEOCBIIOTRCTEARTSEOGCEEAPRHFSOIIOCIRENOUSNSRUETTETCSTHNIIRNIDIBEAIFSLOILHHPTPRLFTHHAGSEROIJTCTCYEENFCRUOLHTNEAESYRSHSLWHCRERMIHPHDYHHJELIATNSHRHCIOETNNOTTIROVSTOMDSESTIAHAOLTHEELTAEDULTOENRVFUNUTOMLTEBEUNCPMYDUPHECEEFEFOOITTNNIBOHBYBBEAOOSROHCELNKRDQOAMILEOMSNAVHOHSCEWEMAIYDNSACEMEARMSEHMLXDESAHTDINFURVBDUHECECEIPOGVITGCTBYEHOHOACSTTOOSRLEHTDRHIOTTAIDOELADARSERIESAIERDT

def readOffHorizontal(userCipherArray):
    index = 0
    output = []
    while index < len(userCipherArray[0]):
        for row in userCipherArray:
            output.append(row[index])
        index += 1
    return "".join(output)

print(readOffVertical(x))
input("")









#WWWESWWEHRASWRASIITAIITXCSCRSSCXHTHESTHX
#decodes to
#WHICHWRISTWATCHESARESWISSWRISTWATCHESXXX

#WHICHWRISTWATCHESARESWISSWRISTWATCHESXXX
#encodes to
#WWWESWWEHRASWRASIITAIITXCSCRSSCXHTHESTHX

#WHICH
#WRIST
#WATCH
#ESARE
#SWISS
#WRIST
#WATCH
#ESXXX



















#==============================================================================================================================================================
#                                                   USER INPUT / OUTPUT                   MAIN PROGRAM
#==============================================================================================================================================================

keyIterations = columularSolvingIndex = REPLACEME123 = 0

#########  Turn each function on or off  #########

# KEY WORD:
columunlarStart = True

# DECLARE USERCIPHER HERE AND COMMENT OUT THE USER INPUT IF YOU ARE WORKING ON THE SAME CIPHER
userCipherNoFormatBypass = "OOHSEERRWCOITUEIEHPIELTINFUTVEOGNRTWDENIIETIGCOATOTIETRCLTLRSESEBHCEOTEOTDONHNETTECNSNCVTAITTUEEUITLAUOTRYDHTLHNURCRITIOAFCMADVSESATIJSTTHNBDOANTTEEEAETHAHILRGEIEEGYNDFTOFREOSKNAHSRLELSTDOODAFLIIIAARNHELBYEEHLHLGHSCTHTBOIUNPTELTRLTESMSIGPTDAEECRAEUDCOLONSEGOFACVALMTBLJNBOHIOAIRNHTMPESRAFABARDGMOEXTESRIGHLSEDERPNGRTEIDEBOIOWRSOILTASRNJRHMTFOTTGNSLHCDSHITRTESLIHNCIWNOPRYEATLSIETEUOYAEEOTGQFNTLSMNEFNRABLWCMUEYHIREEIDEDUTTNNTAOSSNLRNLARBAHNHOERNHDTLOEMDLNNQFIHEECIRFAUARMAPAOEREMEEHSSGSPVRYEDETIIRTEOLYESHSIWCKHNTCOMHSFIOICELEICOADWLOUTCBHEORRATCPELREORPHAFAOETSNFITRSIETYNMIAENTHILAOVTMHHULICAPEIRPELHEOTFAFDOLRSHHYHAREQEHDFPIYTHOISTSOJRMTRUNEBHUHIRLENTLOEILSTICEAYTUNNITNNEAOTNEIGNEISIRLMPAHHSETDCRHNHARTHMWNFRFCSIDIEOIDIEEAVOEROELSEDDHRTTTTSEEHNNSIRIDPNOIIEPUORUEHDETTEOIGUTUYTOODIEEODCHREHHSEAOFMLEHWVSRTRHTSENANIPTVSRISHOEDRELTMTDTOUIDEYERATSERRLNHEGMAEELSETSAIDTLTETDOIHLFPRGAECEOPLHNTAOIEAEMVNPHOSPTIAPLNGSIERTCOEHOPHLTUDLFEKDSCEGEIFARTTLTRUTEPTENAIRCAITEAUHEFSEABIDATTTMUUMIIOTVLPPGYCRTOEOCSAOVRRPAIEIALAAQNEVFNOTRTNRIMFVAGINFRFRMMBNEUUAUTACNDATILMURCRDCOTALGNSAOYRNLHLMETBRDTLRIMFTNTGNTTUTEOEYOHIBWCAEDHEEECNTEUAYIRTONNCIITECLTEHETPTRPUEHMHLNROEYANSEVRDCALSTTUBEUSCTPESGONEHMNCOEIEDLSHWUCLNTAIEEIASITIEUTSGOAFCEESEAEULHVHEFEHHAARONIOFAEORSAOEIIAUNAISTLOTHUITAOTTNUNOPNRSENEIHONJIPYGTPLBEHOEOEOSSTNHXHTCEETRBAIILATYTIDTNMBEUEYFXBPSFLSEEROEIIEASEHYEIOEILADAOFSESETSFRONRNRNTEVUOOEYOISIHMUNEAECSUEOTLEJAEENELEBEGDENDOGSOEKMHRDATRTEYHNEDEHNROVQRRWOMROAACLOHACNHPGIMGUEBSTITCITCRLNTIHIPEUMUSASOEKAAIEMLTNCODSAERNHHNLEURGOAUIRTHGVWBSEARHHOCNLIOSRTOFMHHETETTSLTCEOTCODLIMNEAEHTVYWBSISSSEHHAPLSMIRHEAFASEOTIRIRTTLEAYHTUDREDTTFSIBNOITATSSEODHEPAXLAPFRCVSNIRAEDHROOSMOYPGRMECHWSSEAHTRHCCRRFLEPNMEVEENESAWEEEUESSRDTTHRDOISTMDIEHRNLBUVOOHXEDWESODARNNVOEINOWVASTTIOLOADLTALNHTEUNEETOTPOTSDMRRLTPIETSOWCNDHAANXFIRNSEHUARTTNTRCMNHAWVICTHGCBCIAIUTDVOITSAUKAENCEHDUAPAEEOOFMITCRIILTSERSLIATCIHRDOCEGALTSCINDLAORPTDDHTTOEGESOFGICOIIOVFGMETRISISYIDTARLERRGISEUULCMEETNITLAETUSBTITJMTYOFNSATEEIEAONHSTTELAOTFTNYEHWTOSASOCITTAEAOLPLEOCHLTRICSPNHGUBTOIEODITTIVRIIOORRPEOOMQNBRTSHUSTORRTEIAECLTIOTATEFNRTAEHDNRMUATTUBDIRDTFERSTROEIITSHEDOTREIMTMHEOOHUEIDGTHBMAUCTEIOTHEALOAPAEIESMSLADENKFTPOICPIHREAFCOMHLRLIEFFAYNDURSDAYDLDOAHGPERIRNRSGAISANFDOOEULEGICRRNIOLIILFRARRENIAMAESETNGUNAIOORTOIRSTSFUEOBHARSRIEDANNDDCHLIST"
userCipher = tx.formatString((userCipherNoFormatBypass).lower())

while False == True: #Loops the entire program   
    #userCipher = formatString((input(cipherSolverInputFormat)).lower()) # ensures all ciphertext given to functions is correclty formatted
    #########################################################
    #           Calling different deciphering functions
    #########################################################
    while keyIterations < keyIterations + 1:
        if columunlarStart == True: #Iterative solver
            cipherOut = ""#columunlarSolve(userCipher)
            columularSolvingIndex += 1
        keyIterations += 1
        #########################################################
        #                   Text statistics
        #########################################################
        ### Choose which scoring system you want to rank texts by:
        
        #relationScore = relationToEnglishFrequency(characterFrequencyProbability(cipherOut))
        #indexOfCoincidenceText = round(indexOfCoincidence(cipherOut),10)
        #chiSquaredText = round(chiSquaredStat(cipherOut),10)
        ngramScore = ngramFitness(cipherOut)
        
        # if relationScore < 0.05 and relationScore > -0.05:
        # if indexOfCoincidenceText < 1:
        # if chiSquaredText < 200:
        if ngramScore > -6000: # Change this number here the closer to 0 the less it will accept and print
            indexOfCoincidenceText = round(indexOfCoincidence(cipherOut),10)
            chiSquaredText = round(chiSquaredStat(cipherOut),10)
            ngramScore = ngramFitness(cipherOut)
            relationScore = relationToEnglishFrequency(characterFrequencyProbability(cipherOut))
            readablePlaintext = defrag.words(cipherOut)
            cipherOutKeyOut ='''
==================== PLAINTEXT: ====================
{printedCipherOut}
=================== STATISTICS: ====================
Number of keys              {printedAttempts}
log Ngram Score             {printedNgramScore}
Index Of Coincidence        {printedIoC}
Chi Squared                 {printedChi}
English Frequency Relation  {printedRelationScore}
'''.format(printedCipherOut = readablePlaintext,printedNgramScore = ngramScore,printedAttempts = keyIterations,printedIoC = indexOfCoincidenceText, printedChi = chiSquaredText,printedRelationScore = relationScore)
            print(cipherOutKeyOut)
            jsonData = { 
                "readablePlaintext": readablePlaintext,
                "plaintext": cipherOut,
                "keyLength": keyLength,
                "noOfKeys": keyIterations, 
                "ngramScore": ngramScore, 
                "IOC": indexOfCoincidenceText, 
                "chi2": chiSquaredText, 
                "frequencyRelation": relationScore,
            }
            os.chdir(outputFilesHere)
            with open("outputTransposition.txt", "a") as f:
                f.write(json.dumps(jsonData)+"\n")

                



