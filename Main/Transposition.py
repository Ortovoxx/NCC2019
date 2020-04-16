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

def substitionKeyCipher(userCipherText,userKey): #maps a ciphertext to plaintext according to the key given to it
    cipherText = tx.convertToASCII(list(userCipherText)) #Converting cipher to numbers
    key = tx.convertToASCII(list(userKey)) #Converting key to numbers
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
    return "".join(tx.convertToCHARACTER(switchedCipher))

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

def iterativeSolving(cipherText,maxScore):
    parentText = list(cipherText)
    parentScore = ngramFitness(cipherText)
    count = 0
    while count < 1000:
        a = random.randint(0,25)
        b = random.randint(0,25)
        childText = parentText[:]
        # swap two characters in the child
        childText[a],childText[b] = childText[b],childText[a]
        childScore = ngramFitness("".join(childText))
        # if the child was better, replace the parent with it
        if childScore > parentScore:
            parentScore = childScore
            parentText = childText[:]
            count = 0
        count += 1
        print(childScore)
    # keep track of best score seen so far
    if parentScore > maxScore:
        maxScore = parentScore
        return "".join(parentText)

#==============================================================================================================================================================
#                                                   USER INPUT / OUTPUT                   MAIN PROGRAM
#==============================================================================================================================================================

keyIterations = keyWordAlphabetIndex = keyWordRandomIndex = frequencyKeyIndex = randomKeyIndex = ceaserShifts = iterativeSolvingIndex = shiftNumber = REPLACEME123 = 0
maxScoreIterative = -99e9

#########  Turn each function on or off  #########

# KEY WORD:
iterativeStart = True

# DECLARE USERCIPHER HERE AND COMMENT OUT THE USER INPUT IF YOU ARE WORKING ON THE SAME CIPHER
userCipherNoFormatBypass = "OOHSEERRWCOITUEIEHPIELTINFUTVEOGNRTWDENIIETIGCOATOTIETRCLTLRSESEBHCEOTEOTDONHNETTECNSNCVTAITTUEEUITLAUOTRYDHTLHNURCRITIOAFCMADVSESATIJSTTHNBDOANTTEEEAETHAHILRGEIEEGYNDFTOFREOSKNAHSRLELSTDOODAFLIIIAARNHELBYEEHLHLGHSCTHTBOIUNPTELTRLTESMSIGPTDAEECRAEUDCOLONSEGOFACVALMTBLJNBOHIOAIRNHTMPESRAFABARDGMOEXTESRIGHLSEDERPNGRTEIDEBOIOWRSOILTASRNJRHMTFOTTGNSLHCDSHITRTESLIHNCIWNOPRYEATLSIETEUOYAEEOTGQFNTLSMNEFNRABLWCMUEYHIREEIDEDUTTNNTAOSSNLRNLARBAHNHOERNHDTLOEMDLNNQFIHEECIRFAUARMAPAOEREMEEHSSGSPVRYEDETIIRTEOLYESHSIWCKHNTCOMHSFIOICELEICOADWLOUTCBHEORRATCPELREORPHAFAOETSNFITRSIETYNMIAENTHILAOVTMHHULICAPEIRPELHEOTFAFDOLRSHHYHAREQEHDFPIYTHOISTSOJRMTRUNEBHUHIRLENTLOEILSTICEAYTUNNITNNEAOTNEIGNEISIRLMPAHHSETDCRHNHARTHMWNFRFCSIDIEOIDIEEAVOEROELSEDDHRTTTTSEEHNNSIRIDPNOIIEPUORUEHDETTEOIGUTUYTOODIEEODCHREHHSEAOFMLEHWVSRTRHTSENANIPTVSRISHOEDRELTMTDTOUIDEYERATSERRLNHEGMAEELSETSAIDTLTETDOIHLFPRGAECEOPLHNTAOIEAEMVNPHOSPTIAPLNGSIERTCOEHOPHLTUDLFEKDSCEGEIFARTTLTRUTEPTENAIRCAITEAUHEFSEABIDATTTMUUMIIOTVLPPGYCRTOEOCSAOVRRPAIEIALAAQNEVFNOTRTNRIMFVAGINFRFRMMBNEUUAUTACNDATILMURCRDCOTALGNSAOYRNLHLMETBRDTLRIMFTNTGNTTUTEOEYOHIBWCAEDHEEECNTEUAYIRTONNCIITECLTEHETPTRPUEHMHLNROEYANSEVRDCALSTTUBEUSCTPESGONEHMNCOEIEDLSHWUCLNTAIEEIASITIEUTSGOAFCEESEAEULHVHEFEHHAARONIOFAEORSAOEIIAUNAISTLOTHUITAOTTNUNOPNRSENEIHONJIPYGTPLBEHOEOEOSSTNHXHTCEETRBAIILATYTIDTNMBEUEYFXBPSFLSEEROEIIEASEHYEIOEILADAOFSESETSFRONRNRNTEVUOOEYOISIHMUNEAECSUEOTLEJAEENELEBEGDENDOGSOEKMHRDATRTEYHNEDEHNROVQRRWOMROAACLOHACNHPGIMGUEBSTITCITCRLNTIHIPEUMUSASOEKAAIEMLTNCODSAERNHHNLEURGOAUIRTHGVWBSEARHHOCNLIOSRTOFMHHETETTSLTCEOTCODLIMNEAEHTVYWBSISSSEHHAPLSMIRHEAFASEOTIRIRTTLEAYHTUDREDTTFSIBNOITATSSEODHEPAXLAPFRCVSNIRAEDHROOSMOYPGRMECHWSSEAHTRHCCRRFLEPNMEVEENESAWEEEUESSRDTTHRDOISTMDIEHRNLBUVOOHXEDWESODARNNVOEINOWVASTTIOLOADLTALNHTEUNEETOTPOTSDMRRLTPIETSOWCNDHAANXFIRNSEHUARTTNTRCMNHAWVICTHGCBCIAIUTDVOITSAUKAENCEHDUAPAEEOOFMITCRIILTSERSLIATCIHRDOCEGALTSCINDLAORPTDDHTTOEGESOFGICOIIOVFGMETRISISYIDTARLERRGISEUULCMEETNITLAETUSBTITJMTYOFNSATEEIEAONHSTTELAOTFTNYEHWTOSASOCITTAEAOLPLEOCHLTRICSPNHGUBTOIEODITTIVRIIOORRPEOOMQNBRTSHUSTORRTEIAECLTIOTATEFNRTAEHDNRMUATTUBDIRDTFERSTROEIITSHEDOTREIMTMHEOOHUEIDGTHBMAUCTEIOTHEALOAPAEIESMSLADENKFTPOICPIHREAFCOMHLRLIEFFAYNDURSDAYDLDOAHGPERIRNRSGAISANFDOOEULEGICRRNIOLIILFRARRENIAMAESETNGUNAIOORTOIRSTSFUEOBHARSRIEDANNDDCHLIST"
userCipher = tx.formatString((userCipherNoFormatBypass).lower())

while True: #Loops the entire program   
    #userCipher = formatString((input(cipherSolverInputFormat)).lower()) # ensures all ciphertext given to functions is correclty formatted
    #########################################################
    #           Calling different deciphering functions
    #########################################################
    while keyIterations < keyIterations + 1:
        if iterativeStart == True: #Iterative solver
            cipherOut = iterativeSolving(userCipher, maxScoreIterative)
            iterativeSolvingIndex += 1
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
                "key": userKey,
                "noOfKeys": keyIterations, 
                "ngramScore": ngramScore, 
                "IOC": indexOfCoincidenceText, 
                "chi2": chiSquaredText, 
                "frequencyRelation": relationScore,
            }
            os.chdir(outputFilesHere)
            with open("output.txt", "a") as f:
                f.write(json.dumps(jsonData)+"\n")

                



