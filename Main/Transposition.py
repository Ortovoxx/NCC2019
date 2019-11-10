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
'''

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