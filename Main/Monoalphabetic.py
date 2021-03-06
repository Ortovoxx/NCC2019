#==============================================================================================================================================================
#                                                                          Euan Caskie 
#
#                                                                   National Cipher Challenge
#
#
#                                                             IMPORTANT INFO BEFORE USING THIS PROGRAM:
#
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

keyIterations = 0

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

class wordScore(object): # Finds and segments words so that they can be readable
    os.chdir(wordScoreDir)
    def __init__(self):
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

class timer():
    def __init__(self):
        pass
    
    def start(self):
        self.startTime = time.time()
    
    def end(self):
        self.endTime = time.time()

    def elapsed_S(self):
        return round(self.endTime - self.startTime)
    
    def elapsed_MS(self):
        return round((self.endTime - self.startTime)*1000)
    
    def elapsed_US(self):
        return round((self.endTime - self.startTime)*1000000)

    def elapsed_NS(self):
        return round((self.endTime - self.startTime)*1000000000)

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

def characterFrequency(cipherText): # finds the character frequency of a inputted ciphertext
    frequency = []
    for letter in alphabetCHARACTER: # Iterates through the alphabet 
        total = re.findall(letter,cipherText) # Find each of the occurances of a letter and puts them into list total
        frequency.append(len(total)) # finds the length of the list and appends it to another list 
    return frequency

def characterFrequencyProbability(cipherText): # fidn the character frequency of an inputted ciphertext in probability of it occuring in said text ( % )
    probability = []
    frequency = characterFrequency(cipherText)
    for n in frequency:
        probability.append(round((n / len(cipherText)),5))
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
        lenCipherText = len(cipherText)
        x = (n - 1)
        while index < lenCipherText - x:
            quadIndex = 0
            singleQuadgram = []
            while quadIndex < n and index < lenCipherText:
                if index + quadIndex < lenCipherText:
                    singleQuadgram.append(cipherText[index + quadIndex])
                    quadIndex += 1
            quad = "".join(singleQuadgram)
            if quad in quadramDitionaryCiphertext:
                quadramDitionaryCiphertext[quad] = quadramDitionaryCiphertext[quad] + 1
            else:
                quadramDitionaryCiphertext[quad] = 1
            index += 1
        return quadramDitionaryCiphertext
    
    quadramDitionaryCiphertext = ngramExtraction(userCiperText)
    score = 0
    for index in quadramDitionaryCiphertext: # adds up all the log probabilities of the ciphertext to produce a final score
        if index in ngramDitionaryEnglish:
            score = score + math.log10(ngramDitionaryEnglish[index])
        else:
            score = score - 10000 # log10 of a small positive number approaches -infinity // the bigger this number bigger gap between english and non english words
    return score

def relationToEnglishFrequency(cipherTextFrequency): # Finds the difference between a ciphertext frequency ( % ) and english frequency and outputs a score 
    index = 0
    lists = []
    while index < 25:
        difference = round(englishLetterFrequency[index] - (cipherTextFrequency[index])*100,10)
        lists.append(difference)
        index+=1
    score = sum(lists)
    return round(score,10)

def jsonCipherIn(): # allows for text files containing JSON strings to be inputted
    output = []
    os.chdir(outputFilesHere)
    with open("outputMonoalphabetic.txt", "r") as f:
        jsonIN = f.readlines()
        for i in jsonIN:
            x = json.loads(i)
            plainText = x["plaintext"]
            output.append(plainText)
    return output
    
#==============================================================================================================================================================
#                                                            CIPHER SOLVING - EDITABLE
#==============================================================================================================================================================

def ceaser(string, shift): # Ceaser shift function
    cipher = ""
    for char in string:
      if char == " ":
        cipher = cipher + char #leaves spaces
      else:
        cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97) #Shifts all lowercases
    return cipher

def randomKey(): # Generates a random key
    toShuffle = alphabetCHARACTER
    random.shuffle(toShuffle)
    return "".join(toShuffle)

def keyWordRandom(index): #Keyword key generator - filled in bit being random characters
    lenFreq = len(keyWords)
    if index > lenFreq - 1:
        index = index - ( ( index // lenFreq ) * lenFreq )
    key = tx.convertToASCII(list(keyWords[index]))
    countIndex = 0
    while countIndex < 26: #Removes duplicate letters any words may have
        howMany = key.count(alphabetASCII[countIndex])
        if howMany >= 2:
            where = key.index(alphabetASCII[countIndex])
            while howMany > 1:
                key.pop(where)
                where = key.index(alphabetASCII[countIndex])
                howMany -= 1
        countIndex += 1
    perms = len(key)
    while perms < 26: #Ensures 26 letters in the alphabet
        randomNo = random.randint(97, 122)
        repeat = tx.search(randomNo,key) #Ensures each letter is unique
        if repeat == False:
            key.append(randomNo)
            perms += 1
    return "".join(tx.convertToCHARACTER(key))

def keyWordAlphabet(index): #Keyword key generator - filled in bit being the alphabet - keyed ceaser
    lenFreq = len(keyWords)
    if index > lenFreq - 1:
        index = index - ( ( index // lenFreq ) * lenFreq )
    key = tx.convertToASCII(list(keyWords[index]))
    countIndex = 0
    while countIndex < 26: #Removes duplicate letters any words may have
        howMany = key.count(alphabetASCII[countIndex])
        if howMany >= 2:
            where = key.index(alphabetASCII[countIndex])
            while howMany > 1:
                key.pop(where)
                where = key.index(alphabetASCII[countIndex])
                howMany -= 1
        countIndex += 1
    perms = 0
    repeat = False
    while perms < 26: #Ensures 26 letters in the alphabet
        newChar = alphabetASCII[perms]
        repeat = tx.search(newChar,key) #Ensures each letter is unique
        if repeat == False:
            key.append(newChar)
        perms += 1
    return "".join(tx.convertToCHARACTER(key))

def keyWordCeaser(index,shiftIndex): #Keyword key generator - filled in bit being the alphabet which is then shifted 26 times for the same keyword
    lenFreq = len(keyWords)
    if index > lenFreq - 1:
        index = index - ( ( index // lenFreq ) * lenFreq )
    key = tx.convertToASCII(list(keyWords[index]))
    countIndex = 0
    while countIndex < 26: #Removes duplicate letters any words may have
        howMany = key.count(alphabetASCII[countIndex])
        if howMany >= 2:
            where = key.index(alphabetASCII[countIndex])
            while howMany > 1:
                key.pop(where)
                where = key.index(alphabetASCII[countIndex])
                howMany -= 1
        countIndex += 1
    perms = 0
    repeat = False
    endKey = []
    while perms < 26: #Ensures 26 letters in the alphabet
        newChar = alphabetASCII[perms]
        repeat = tx.search(newChar,key) #Ensures each letter is unique
        if repeat == False:
            endKey.append(newChar) # adds all the extra characters to a new list to be shifted later
        perms += 1
    shiftedEnd = tx.shiftRight(endKey,shiftIndex) # shifts a list "shiftIndex" places to the right
    keyStart = "".join(tx.convertToCHARACTER(key))
    shiftedEnd = "".join(tx.convertToCHARACTER(shiftedEnd))
    return keyStart + shiftedEnd # joins the two first keyword and the rest of the shifted string together to make an entire key

def searchFrequencyAnalysis(itemToCheckFor): #Compares the inputted value to standard english language letter freuqnecy and finds the closest value and returns its letter position (a=0 b=1 etc) [all in %]

    def searchFrequencyAnalysisSorted(positionToMap): #Takes both the sorted alphabet and normal alphabet and maps the positions from the ciphertext frequency analysis
        value = englishLetterFrequencySorted[positionToMap]
        mappedPosition = englishLetterFrequency.index(value)
        return mappedPosition
    
    position = 0
    betweenValues = positionSortedAlphabetZero = False
    while position < 26 and not betweenValues:
        if englishLetterFrequencySorted[position] > itemToCheckFor: #compares to the first, and because sorted, highest value and if it is less than it will move onto the second ( next highest)
            if position == 25: #If a value lower than the lowest value is inputted it will bypass everything else (ie input of 0 or less than 0.074)
                positionSortedAlphabetZero = True
            position += 1
        elif englishLetterFrequencySorted[position] < itemToCheckFor: #Does the above until it it greater than the next value so it must be between position and the previous position ( position - 1 )
            betweenValues = True
        if betweenValues == True: #its greater than the position but less than position - 1
            differenceAbove = round(englishLetterFrequencySorted[(position - 1)] - itemToCheckFor,10)
            differentBelow = round(itemToCheckFor - englishLetterFrequencySorted[position],10)
            if differenceAbove > differentBelow and positionSortedAlphabetZero == False: # if the upper different is bigger it is closer to position
                positionSortedAlphabet = position
            elif differenceAbove < differentBelow and positionSortedAlphabetZero == False: # if the lower different is bigger it is closer to position - 1
                if position != 0: 
                    positionSortedAlphabet = position - 1
                else: # if bigger than 12.702 and therefore first or 0th
                    positionSortedAlphabet = position
            positionIndexed = searchFrequencyAnalysisSorted(positionSortedAlphabet)#translates the indexing from the sorted alphabet into the normal alphabet
        elif positionSortedAlphabetZero == True: #Bypass for inputs less than 0.074
            positionSortedAlphabet = 25
            positionIndexed = searchFrequencyAnalysisSorted(positionSortedAlphabet)#translates the indexing from the sorted alphabet into the normal alphabet
    return positionIndexed

def frequencyKey(cipherTextToBeFREQQED): #Function to return the key with accordance to comparisons between the ciphertext frequency analysis and the frequency analysis of english plaintext
    #cipherTextToBeFREQQED is a user inputted string
    frequencyOfCipherText = characterFrequency(cipherTextToBeFREQQED) #gets the frequency analysis data of the string inputted
    cipherTextNoSpaces = cipherTextToBeFREQQED #removes spaces and punctuation of ciphertext
    cipherTextNoSpacesList = list(cipherTextNoSpaces) #converts the formatted ciphertext into an list
    indexOfFrequencyAnalysis = 0
    while indexOfFrequencyAnalysis < 26: #Converts frequency analysis data from number of occurrences into a % of text frequency analysis
        frequencyOfCipherText[indexOfFrequencyAnalysis] = round(((frequencyOfCipherText[indexOfFrequencyAnalysis] / len(cipherTextNoSpacesList))*100),3 )
        indexOfFrequencyAnalysis += 1
    indexToCompare = loopIteration = 0
    englishIndexOrderList = []
    randomIncrease = 100
    lowerRandom = -2
    upperRandom = 2
    while indexToCompare < 26: 
        #Matches the frequencies of individual letters in the ciphertext to that of english producing a key
        #Gets the frequency of ciphertext in % and compares it to the % of english and then returns an list with the positions of the closest values
        englishIndex = searchFrequencyAnalysis(frequencyOfCipherText[indexToCompare])
        duplicates = False
        unCertainty = random.randint(lowerRandom,upperRandom) #Adds uncertainty to the letters so higher chance of finding a correct key (bigger numbers longer key generation time)
        randomisedEnglishIndex = englishIndex + unCertainty
        duplicates = tx.search(randomisedEnglishIndex,englishIndexOrderList) #Ensures no duplicates of positions
        if duplicates == False and randomisedEnglishIndex < 27 and randomisedEnglishIndex > 0:
            englishIndexOrderList.append(randomisedEnglishIndex) #adds each letter mapped to the new letter position to this list (a=0 b=1 etc etc)
            indexToCompare = indexToCompare + 1 #Only increases if there is no duplicates and therefore something new got added else it will repeat until this does happen
        if loopIteration == randomIncrease: # to stop an endless cycle if it has looped 100 times without successfully finding a letter it increases the randomness until it eventually works
            lowerRandom += -1
            upperRandom += 1
            randomIncrease += 200
        loopIteration += 1
    convertASCIIIndex = 0 # Text formatting
    while convertASCIIIndex < 26: #converts the a=0 b=1 (positional data) to ASCII numbers
        englishIndexOrderList[convertASCIIIndex] = englishIndexOrderList[convertASCIIIndex] + 96
        convertASCIIIndex += 1
    return "".join(tx.convertToCHARACTER(englishIndexOrderList)) #converts the ASCII index to a plaintext string key with 26 characters

def iterativeSolving(cipherText): # Hill climb function which iterates slowly through keys until a good match is found
    global keyIterations
    maxScore = -99e9
    parentKey = list(randomKey()) #parentKey = randomKey()#frequencyKey(userCipherText) #parent Key is generated using frequency analysis
    deciphered = substitionKeyCipher(cipherText,"".join(parentKey))
    parentScore = ngramFitness(deciphered)
    count = 0
    while count < 1000:
        a = random.randint(0,25)
        b = random.randint(0,25)
        childKey = parentKey[:]
        # swap two characters in the child
        childKey[a],childKey[b] = childKey[b],childKey[a]
        deciphered = substitionKeyCipher(cipherText,"".join(childKey))
        childScore = ngramFitness(deciphered)
        # if the child was better, replace the parent with it
        if childScore > parentScore:
            parentScore = childScore
            parentKey = childKey[:]
            count = 0
        count += 1
        keyIterations += 1
    # keep track of best score seen so far
    if parentScore > maxScore:
        maxScore = parentScore
        return "".join(parentKey)

def manualKeySwitch(cipherText): # Allows users to manurally switch letters around # borealistuvwxyzcdfghjkmnpq
    key = input("User key: ")
    keyList = list(key)
    toRemove = str(input("What is the incorrect char: ")).lower()
    toAdd = str(input("What do you want to change it to: ")).lower() ###### all the below will need switching around and testing I do now know if I have gotten it right
    toRemovePos = re.search(toRemove,key)
    toAddPos = re.search(toAdd,key)
    keyList.pop(toRemovePos)
    keyList.insert(toRemovePos,toAdd)
    keyList.pop(toAddPos)
    keyList.insert(toAddPos,toRemove)
    print("".join(keyList))

#==============================================================================================================================================================
#                                                   USER INPUT / OUTPUT                   MAIN PROGRAM
#==============================================================================================================================================================

# add a english word length probablity ( take average word length and compare it to that of the plaintext)
# add a way to manuallly manipulate the key 
# add matplot lib graphs for frequency analysis
# add a json input

userKey = "abcdefghijklmnopqrstuvwxyz" #Sets a defult user key ~~~~WARNING~~~~ Wont show error if there is not a key generated as this one will take over ~~~~WARNING~~~~
keyWordAlphabetIndex = keyWordRandomIndex = frequencyKeyIndex = randomKeyIndex = ceaserShifts = iterativeSolvingIndex = shiftNumber = REPLACEME123 = 0

#########  Turn each function on or off  #########

# KEY WORD:
keyWordAlphabetStart = False
keyWordRandomStart = False
keyWordCeaserStart = False
# ADVANCED ANALYSIS
frequencyKeyStart = False
iterativeSolvingStart = True
# CRYPTOGRAPHIC FUNCTIONS
ceaserStart = False
randomKeyStart = False

# DECLARE USERCIPHER HERE AND COMMENT OUT THE USER INPUT IF YOU ARE WORKING ON THE SAME CIPHER
ciphers = ["WSIJK BYYKSCT DW VSY HZARYBSJKYC ADBBSKKYY, IYSARJYIQSYRLCTJBSCSJKYISLB, KNYCKP CSCKR HFISZ CSCYKYYC KRSIKP CSCYKRY ADBBSKKYY NHJ IYADCMYCYV EP KRY BSCSJKYI HK KRY IYGLYJK DW KRY ARHCAYZZDI RSBJYZW.SK SJ KHJXYV NSKR IYHZSJSCT KRY BSZSKHIP HCV SCVLJKISHZ FIDBSJY DW CLAZYHI YCYITP.KRY ADBBSKKYY IYADTCSJYJ KRY KYARCSAHZ ARHZZYCTYJ SCMDZMYV SC SCVLJKISHZSJSCT KRY FIDAYJJYJ RSKRYIKD ADCVLAKYV LCVYI ZHEDIHKDIP ADCVSKSDCJ, ELK WYYZJ KRHK KRY DEJKHAZYJ AHC EY DMYIADBY EP H ADBESCHKSDC DW JASYCKSWSA HCV YCTSCYYISCT YOAYZZYCAY HZIYHVP FDJJYJJYV EP KRY JKHKY.KRY ADBBSKKYY SVYCKSWSYV KRHK KRY FISCASFZY SJJLY SJ KRHK DW ADCKIDZZSCT KRY CLAZYHI IYHAKSDC NRSAR SJ BYVSHKYV EP KRY YCYITP DW WIYY CYLKIDCJ. KRYJY CYYV KD EY JZDNYV KD YWWYAKSMYZP RHICYJJ KRYSI FDNYI, HCV KD KRSJ YCV KRY ADBBSKKYY IYADBBYCVJ KRY HAGLSJSKSDC DW H JLSKHEZY BDVYIHKDI.KRY EYJK-XCDNC AHCVSVHKY SJ VYLKYISLB HCV KRY EYJK JDLIAY DW KRSJ BHKYISHZ SJ KRY FDNYI FZHCK HK MYBDIX SC CDINHP. KRY KIDCJKHV HCV EILC YZYAKIDZPKSA FIDAYJJ HK KRHK WHASZSKP SJ FIDVLASCT DMYI KNYCKP XSZDTIHBJ DW RYHMP NHKYI FYI PYHI, HCV KRSJ ADLZV YHJSZP EY JAHZYV LF.JSCAY NY VD CDK NHCK KD HZYIK DLI YCYBSYJ KD KRY SBFDIKHCAY DW KRY BHKYISHZ KRY ADBBSKKYY IYADBBYCVJ FZHASCT HC SCSKSHZ DIVYI WDI WSMY ZSKIYJ DW RYHMP NHKYI KRIDLTR DLI DNC VPY SCVLJKIP JPCVSAHKY ADIFDIHKSDC NRSAR, EP RHFFP HAASVYCK, DNCJ H GLHIKYI DW KRY JRHIYJ SC KRY MYBDIX FZHCK."]

#ciphers = jsonCipherIn() # comment out if just doing a single cipher

while 1: #Loops the entire program   
    #userCipher = formatString((input(cipherSolverInputFormat)).lower()) # ensures all ciphertext given to functions is correclty formatted
    #########################################################
    #           Calling different deciphering functions
    #########################################################
    for userCipherNoFormat in ciphers:
        userCipher = tx.formatString((userCipherNoFormat).lower())
        while keyIterations < 10000000: # how many key iterations you want to spend on one cipher
            if ceaserStart == True: #Ceaser shifts done 26 times
                userKey = ceaser("abcdefghijklmnopqrstuvwxyz", 26 - ceaserShifts)
                cipherOut = ceaser(userCipher, ceaserShifts)
                ceaserShifts += 1
            elif keyWordAlphabetStart == True: # Keyword keys done for all key words with the last letters being random
                userKey = keyWordAlphabet(keyWordAlphabetIndex)
                cipherOut = substitionKeyCipher(userCipher,userKey)
                keyWordAlphabetIndex += 1
            elif keyWordRandomStart == True: # Keyword keys done for all key words with the last letters being the alphabet
                userKey = keyWordRandom(keyWordRandomIndex)
                cipherOut = substitionKeyCipher(userCipher,userKey)
            elif keyWordCeaserStart == True: # Keyword keys done for all key words with the last letters being the alphabet
                userKey = keyWordCeaser(keyWordRandomIndex,shiftNumber)
                cipherOut = substitionKeyCipher(userCipher,userKey)
                if shiftNumber > 26:
                    shiftNumber = 1
                    keyWordRandomIndex += 1
                shiftNumber += 1
            elif frequencyKeyStart == True: #Key generated from advanced frequency analysis
                userKey = frequencyKey(userCipher)
                cipherOut = substitionKeyCipher(userCipher,userKey)
                frequencyKeyIndex += 1
            elif randomKeyStart == True: # Last resort random keys
                userKey = randomKey()
                cipherOut = substitionKeyCipher(userCipher,userKey)
                randomKeyIndex += 1
            elif iterativeSolvingStart == True: # Iterative key solving -- most efficient
                userKey = iterativeSolving(userCipher)
                cipherOut = substitionKeyCipher(userCipher,userKey)
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
            if ngramScore > -3000: # Change this number here the closer to 0 the less it will accept and print
                indexOfCoincidenceText = round(indexOfCoincidence(cipherOut),10)
                chiSquaredText = round(chiSquaredStat(cipherOut),10)
                ngramScore = ngramFitness(cipherOut)
                relationScore = relationToEnglishFrequency(characterFrequencyProbability(cipherOut))
                readablePlaintext = defrag.words(cipherOut)
                cipherOutKeyOut ='''
==================== PLAINTEXT: ====================
{printedCipherOut}
======================= KEY: =======================
{printedUserKey}
=================== STATISTICS: ====================
Number of keys              {printedAttempts}
log Ngram Score             {printedNgramScore}
Index Of Coincidence        {printedIoC}
Chi Squared                 {printedChi}
English Frequency Relation  {printedRelationScore}
'''.format(printedCipherOut = readablePlaintext,
                printedUserKey = userKey,
                printedNgramScore = ngramScore,
                printedAttempts = keyIterations,
                printedIoC = indexOfCoincidenceText, 
                printedChi = chiSquaredText,
                printedRelationScore = relationScore)
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
                with open("outputMonoalphabetic.txt", "a") as f:
                    f.write(json.dumps(jsonData)+"\n")

                