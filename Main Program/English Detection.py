freqWords = ["the","be","of","and","a","to","in","he","have","it","that","for","they","i","with","as","not","on","she","at","by","this","we","you","do","but","from","or","which","one","would","all","will","there","say","who","make","when","can","more","if","no","man","out","other","so","what","time","up","go","about","than","into","could","state","only","new","year","some","take","come","these","know","see","use","get","like","then","first","any","work","now","may","such","give","over","think","most","even","find","day","also","after","way","many","must","look","before","great","back","through","long","where","much","should","well","people","down","own","just","because","good","each","those","feel","seem","how","high","too","place","little","world","very","still","nation","hand","old","life","tell","write","become","here","show","house","both","between","need","mean","call","develop","under","last","right","move","thing","general","school","never","same","another","begin","while","number","part","turn","real","leave","might","want","point","form","off","child","few","small","since","against","ask","late","home","interest","large","person","end","open","public","follow","during","present","without","again","hold","govern","around","possible","head","consider","word","program","problem","however","lead","system","set","order","eye","plan","run","keep","face","fact","group","play","stand","increase","early","course","change","help","line",]



def encrypt(string, shift): # Ceaser shift function
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  return cipher

def searchWords(cipherWord,freqWords): # Linear search to check if a word is English or not by comparing it to the freqWords array
    freqPosition = 0
    cipherPosition = 0
    english = False
    while freqPosition < len(freqWords) and not english:
        if freqWords[freqPosition] == cipherWord:
            english = True
        freqPosition = freqPosition + 1
    return english

def clearScore(cipherPermsArray):
    attempt = 0 
    while attempt < len(cipherPermsArray):
        cipherTextEnglish = cipherPermsArray[attempt]
        cipherTextSplit = cipherTextEnglish.split() #Takes the user input of the cipher and puts it into an array with each field being a different word
        cipherPosition = 0
        while cipherPosition < len(cipherTextSplit): #Sends each word from the input through the function to check if it is english
            cipherEnglish = searchWords(cipherTextSplit[cipherPosition],freqWords)
            cipherEnglishArray.append(cipherEnglish)
            cipherPosition = cipherPosition + 1 
        trues = cipherEnglishArray.count(True) 
        clearScore = round((trues / len(cipherEnglishArray)) * 100) #Calculates the % chance of a text being english
        attempt = attempt + 1
        cipherEnglishArray.clear()
        if clearScore > 30:
            return cipherPermsArray[attempt], clearScore

cipherPermsArray = []
cipherEnglishArray = []


 
cipherText = input("enter ciphertext: ")
shifts = 0
while shifts < 26: #tries every key
    cipherPerms = encrypt(cipherText, shifts)
    cipherPermsArray.append(cipherPerms)
    shifts = shifts + 1


x = clearScore(cipherPermsArray)
print(x)




    




