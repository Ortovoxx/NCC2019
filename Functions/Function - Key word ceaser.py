#==============================================================================================================================================================
#                                                                  VARIABLES, CONSTANTS AND FORMATTING - DO NOT EDIT
#==============================================================================================================================================================

#Modules to imports
import random
import os
import math
import time
import requests
import re

############# IMPORTANT INFO BEFORE USING THIS PROGRAM #############
# Ensure you have an ngram.txt file in the correct directory:
loadEnglishNgramDirectory = "/Users/Euan/Desktop/NCC2019/Cryptanalysis/Text_training_data"
loadKeyWordsDirectory = "/Users/Euan/Desktop/NCC2019/Cryptanalysis"
# All functions should transfer data using lowercase no space no punctuation strings

#########  TEST CIPHERS TO TRY AND SOLVE  #########
#rbo rpktigo vcrb bwucja wj kloj hcjd km sktpqo cq rbwr loklgo vcgg cjqcqr kj skhcja wgkja wjd rpycja rk ltr rbcjaq cj cr
#Tjf, B sppx r ippx rs sqj ubij vpd hjes pojw rey bs zrh mdhs r wpsrsbpe nbaqjw raaibjy sp sqj sjks. Rs ubwhs bs zrh qrwy sp hrv bu sqrs zrh r cdf pw r ujrsdwj rey epwtriiv B zpdiy rhhdtj cdf, cds bs hjjtjy pyy sqrs bs zrh sqj peiv ubij sqrs zrh ruujnsjy hp B rhxjy rwpdey sp hjj bu revpej qry hjje revsqbef hbtbirw. Bs sdweh pds sqrs sqbh zrh eps sqj ubwhs erobfrsbpe awpcijt sp qbs sqj awpfwrttj. Fjej wjapwsjy r trmpw bhhdj zbsq sqj fdbyrenj awpfwrttj upw Heppav pe sqj Rapiip Sje tbhhbpe zqbnq npdiy rfrbe qroj nrdhjy r trmpw awpcijt. Upw hptj wjrhpe sqj awpfwrttj npeswpiibef sqj ireybef wryrw zrhe’s dayrsjy zbsq sqj uibfqs aire rey bu Fjej qrye’s wrbhjy sqrs zbsq Bojwhpe sqje sqj cpvh tbfqs qroj qry wjri swpdcij fjssbef crnx. B ippxjy sqwpdfq sqj nptarev ubijh rey updey repsqjw pu pdw tvhsjwbpdhiv upwtrssjy wjapwsh: sqj tjtp beupwtbef sqjt rcpds sqj nqrefj, zqbnq jkairbeh zqv sqj awpfwrttj ejojw fps dayrsjy. Sqbh sbtj sqj nbaqjw zrh re ruubej hqbus, hp hibfqsiv qrwyjw sp nwrnx, cds epsqbef hjwbpdh. Hsbii, bs bh tdnq ijhh ibxjiv sqrs bs zrh r cdf sqrs sbtj, rey be rev nrhj szbnj bh spp tdnq pu r npbenbyjenj. Bs yby hsrws tj zpeyjwbef zqv sqj hjnpey nbaqjw zrh jrhbjw sp nwrnx sqre sqj ubwhs, cds sqje B wjribhjy sqrs sqj ruubej hqbus zrh spp tdnq pu r fbojrzrv. R wpsrsbpe nbaqjw wjriiv npdiy mdhs cj re jenpybef jwwpw, cds sqj ruubej hqbus bh spp hpaqbhsbnrsjy upw r tbhsrxj, hp zqpjojw trefijy sqj wjapwsh tdhs qroj wjribhjy sqjv qry tryj r cbs pu re jwwpw zbsq sqj ubwhs pej rey swbjy sp npojw sqjbw hsjah zbsq sqj hjnpey. Bs bh qrwy sp hjj sqbh rh revsqbef psqjw sqre rssjtasjy hrcpsrfj, cds B rt eps hdwj zqrs sqj tpsboj npdiy cj. B ypdcs bs bh ajwhperi. Sqj Rapiip Sje rey Jijoje nwjzh ype’s pojwira, hp jbsqjw hptjpej qrh r fwdyfj rfrbehs sqj zqpij Rhswperds npwah pw sqjv rwj swvbef sp yjwrbi sqj Rapiip awpfwrttj. Bs npdiy cj sqj Hpobjsh B hdaaphj. Rs ubwhs, B sqpdfqs sqrs sqjbw zbiibefejhh sp hqbus sqj IDER-UBUSJJE pwcbs hqpzjy sqrs sqjv zjwje’s arws pu bs, cds hptjpej be sqj Hsrsj Yjarwstjes apbesjy pds sqrs sqjv tbfqs mdhs qroj qry r fdbisv npehnbjenj, pw cjje xjje sp ybhsrenj sqjthjiojh penj sqj aips zrh ybhnpojwjy. B rt hsbii eps hdwj. Be sqj tjresbtj, npdiy vpd srxj r ippx rs sqj nptadsjw ubijh sp hjj zqp tbfqs qroj qry rnnjhh sp cpsq tjtph, rey zqp tbfqs qroj qry sqj paapwsdebsv rey tjreh sp ypnspw sqjt? B rt uivbef crnx sp Irefijv spebfqs, sp hjj bu sqj Hsrsj Yjarwstjes qroj rev byjrh zqrs tbfqs cj fpbef pe. Ejbi hrby qj npdiy uiv tj da be pej pu sqj ERHR nqrhj airejh, zqbnq bh hptjsqbef B qroj cjje xjje sp swv. B zbii nrii vpd bu B fjs revsqbef.
#xqhho y qc dej ikhu yv oek muhu sefyut yd je jxu cuce qrekj husudj uludji rkj xuhu yi q ikccqho jme tqoi qwe qd evvtkjo wkytqdsu evvysuh qbuhjut cyiiyed sedjheb je q fejudjyqb fherbuc myjx jxu qfebbe vbywxj jxu fbqddut tuisudj jhqzusjeho qffuqhut je ru hkddydw ed q sebbyiyed sekhiu myjx
#WKMPC ZKXDV SYEZU KYLTV ICYFK BVDDN KZKXD VMYXO BPKLP XMDNK CDVLL VXTDB IPXMD YMVEM KDNKW YYTDN KBKIY EVBKB PMNDD NKNVG RCVBK MKDDP XMZBK DDIBK CDUKC CVXTN VFKWY BKYBU KCCTK SPTKT VUBKV TIDNV DDNKC YFPKD CVBKD YOUVW KLYBB KSKXD KFKXD CYXDN KVZYU UYZBY MBVWW KCYWK YLDNK MKXKB VUCTY XDXKK TWESN YLVXK HSECK DYDEB XEZDN KNKVD OEDIY ETYXD MKDLY EBCDV BCGPD NYEDE XTKBC DVXTP XMDNK XKKTL YBZYU PDPSV UCEZZ YBDVX TDNKB KNVCO KKXVS YXSKB DKTGN PCZKB PXMSV WZVPM XDYSY XFPXS KDNKZ BKCPT KXDDY DVRKV CDBYX MUPXK DNKWY CDCDB PTKXD VBKSV UUPXM LYBVU VBMKO EPUTE ZYLLY BSKCV UYXMD NKOYB TKBGP DNKVC DMKBW VXIVC VCNYG YLCDB KXMDN VBMEP XMDNV DDNKV DDVSR YXDNK CZVSK ZBYMB VWWKW ECDNV FKOKK XVEDN YBPCK TOIDN KZYUP DOEBY DNVDW VRKCX YCKXC KDYWK LPBCD DNKBE CCPVX CVBKW YBKUP RKUID YDBID YGPXD NKZBY ZVMVX TVGVB DNVXD YBPCR SYXLU PSDVX TCKSY XTDNK CVOYD VMKPL DNVDP CGNVD PDPCP CXDCY ZNPCD PSVDK TKXYE MNLYB VRMOY ZKBVD PYXOE DPDPC NVBTD YSYXF PXSKD NKMKX KBVUC DNVDD NVDPC DBEKC YWKYL DNKWY BKSVE DPYEC ZUVXX KBCWY CDUID NYCKG NYVSD EVUUI LYEMN DPXDN KUVCD GVBNV FKWVX VMKTD YOUYS RDNKO EPUTE ZZBYZ YCPXM VXKGD BVXSN KYLGV BMVWK CPXCD KVTWY OPUPC PXMDN VDGVI PCCDP UUVZB YFYSV DPYXO EDPCU KCCUP RKUID YVSSP TKXDV UUIDB PMMKB VGVBK CZKSP VUUIP LGKXY DPLIZ VFUYF CRIPX VTFVX SKVUU DNKCV WKWIY GXDPW KPXOK BUPXS YXFPX SKTWK GKNVF KDYDB KVTFK BICYL DUIDN KBKCY PNKVT KTYFK BDYUV XMUKI VXTSY XFPXS KTDNK WDYCE MMKCD VXVUD KBXVD PFKGK GPUUC DKZEZ PXCZK SDPYX CVDSN KSRZY PXDSN VBUPK DYWVR KPDNV BTKBL YBCYF PKDVM KXDCD YSBYC CVXTS BVXRE ZDNKD KELKU COKBM UPCDK XPXMY ZKBVD PYXDY CKKPL DNVDD EBXCE ZVXID NPXMB KUVDK TPVWV UCYMY PXMDY CKXTV SYEZU KYLYE BOKCD YFKBD YOVPR YXEBD YDBIV XTLPX TYEDG NVDPC MYPXM YXDNK BKDNK CYFPK DCVBK ZBKDD ICKSB KDPFK VOYED DNKPB YGXCZ VSKZB YMBVW WKVXT GPDNY EDDNK GYBUT CZBKC CGVDS NPXMG KTYXD BKVUU INVFK VSUKV BZPSD EBKYL DNKPB ZBYMB KCCYB DNKPB ZUVXC EXUKC CDNKI VBKSU YCKDY ZEDDP XMDNK PBYGX WKXYX DNKWY YXPSV XDCKK GNVDD NKINV FKDYM VPXGP DNGNV DCKKW CDYOK VLVPB UITPC YBMVX PCKTV DDKWZ DDYTK BVPUY EBCZV SKZBY MBVWW KOEDP GYEUT CDPUU UPRKD YRXYG GNVDD NKIVB KEZDY RKKZV SUYCK KIKYX DNKWP CCPYX ZUVXX PXMVX TUKDW KRXYG PLIYE NKVBV XIDNP XMGYB BIPXM PGPUU OKOVS RVOYE DVGKK ROKLY BKDNK UVEXS NNVBB I
#pmpafxaikkitprdsikcplifhwceigixkirradfeirdgkipgigudkcekiigpwrpucikceiginasikwduearrxiiqepcceindgmieinpwdfprduppcedoikiqiasafmfddfipfgmdafmfdteiki

# WORK ON EFFICIENCY OF FILES TODO:
# Find some typical log probabilities for english texts and for texts with different ciphers put through them to get a rough guage of how fit it is
# Make ngram fitness more efficent
# Add functions to different files then import them into main program
# Add extra words to the list to get better accuracy when detecting english and generating key

#Menu and input formats
cipherSolverInputFormat = '''*************** CIPHERTEXT: **************
'''
textManipulationInputFormat = '''*********** INPUT YOUR TEXT: ***********
'''

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

#==============================================================================================================================================================
#                                                       TEXT MANIPULATION AND REPEATED USE FUNCTIONS - DO NOT EDIT
#==============================================================================================================================================================

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
def substitionKeyCipher(userCipherText,userKey): #maps a ciphertext to plaintext according to the key given to it
    cipherText = convertToASCII(list(userCipherText)) #Converting cipher to numbers
    key = convertToASCII(list(userKey)) #Converting key to numbers
    def switchChar(cipherChar): #Switches a single character from its chiphertext to its plaintext
        alphaPerm = 0
        newChar = 0
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
    switchedCipherStr = "".join(convertToCHARACTER(switchedCipher))
    return switchedCipherStr
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
'''
permsCC = 0
new = True

keyCeaser = []

def keyWordCeaser(index): #Keyword key generator - filled in bit being the alphabet
    fuck = True
    while new == True and fuck == True:
        lenFreq = len(keyWords)
        if index > lenFreq - 1:
            index = index - ( ( index // lenFreq ) * lenFreq )
        key = convertToASCII(list(keyWords[index]))
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
        fuck = False
    perms = 0
    repeat = False
    keyCeaser = []
    while perms < 26: #Ensures 26 letters in the alphabet
        newChar = alphabetASCII[perms]
        repeat = search(newChar,key) #Ensures each letter is unique
        if repeat == False:
            keyCeaser.append(newChar)
        perms += 1
    popped = keyCeaser.pop(0)
    keyCeaser.append(popped)
    for n in keyCeaser:
        key.append(n)
    #permsCC+=1
    #if permsCC == len(keyCeaser):
        #new = neww
        #permsCC = permsCCC
        #keyCeaser = keyCeaserr

    return "".join(convertToCHARACTER(key))


'''





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


def shiftRight(a,r):
    index = 0
    while index < r:
        x = a.pop()
        a.insert(0, x)
        index+=1
    return a


def keyWordCeaser(index,shiftIndex): #Keyword key generator - filled in bit being the alphabet
    lenFreq = len(keyWords)
    if index > lenFreq - 1:
        index = index - ( ( index // lenFreq ) * lenFreq )
    key = convertToASCII(list(keyWords[index]))
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
        repeat = search(newChar,key) #Ensures each letter is unique
        if repeat == False:
            endKey.append(newChar)
        perms += 1
    shiftedEnd = shiftRight(endKey,shiftIndex)
    keyStart = "".join(convertToCHARACTER(key))
    shiftedEnd = "".join(convertToCHARACTER(shiftedEnd))
    return keyStart + shiftedEnd




i=0
c=1
while i < 1000000:
    x = keyWordCeaser(i,c)
    print(x)
    c+=1
    if c > 26:
        c = 1
        i+=1

    #,new,permsCC,keyCeaser

#abcdefghijklmnopqrstuvwxyz
#advnturesxyzbcfghijklmopqw