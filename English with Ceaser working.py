freqWords = ["the","be","of","and","a","to","in","he","have","it","that","for","they","i","with","as","not","on","she","at","by","this","we","you","do","but","from","or","which","one","would","all","will","there","say","who","make","when","can","more","if","no","man","out","other","so","what","time","up","go","about","than","into","could","state","only","new","year","some","take","come","these","know","see","use","get","like","then","first","any","work","now","may","such","give","over","think","most","even","find","day","also","after","way","many","must","look","before","great","back","through","long","where","much","should","well","people","down","own","just","because","good","each","those","feel","seem","how","high","too","place","little","world","very","still","nation","hand","old","life","tell","write","become","here","show","house","both","between","need","mean","call","develop","under","last","right","move","thing","general","school","never","same","another","begin","while","number","part","turn","real","leave","might","want","point","form","off","child","few","small","since","against","ask","late","home","interest","large","person","end","open","public","follow","during","present","without","again","hold","govern","around","possible","head","consider","word","program","problem","however","lead","system","set","order","eye","plan","run","keep","face","fact","group","play","stand","increase","early","course","change","help","line"]
'''
TO DO LIST
- TEXT MANIPULATOR
- REMOVE PUNCTUATION
- REMOVE / ADD SPACES
- MAKE UPPER AND LOWER CASE
- REVERSE EVERYTHING
- KEYED SUBSTITUTION
- KEY GENERATOR
'''
def clearScoreEnglish(cipherText): # clear Score function that returns % english when string inputted 
    def searchWords(cipherWord,freqWords):
        freqPosition = 0
        english = False
        while freqPosition < len(freqWords) and not english: # Linear searches a specific word with the english language
            if freqWords[freqPosition] == cipherWord:
                english = True
            freqPosition = freqPosition + 1
        return english
    cipherEnglishArray = []
    cipherTextSplit = cipherText.split()
    cipherPosition = 0
    while cipherPosition < len(cipherTextSplit):
        cipherEnglish = searchWords(cipherTextSplit[cipherPosition],freqWords) 
        cipherEnglishArray.append(cipherEnglish) # puts all the T's and F's into an array
        cipherPosition = cipherPosition + 1
    trues = cipherEnglishArray.count(True)
    clearScore = round((trues / len(cipherEnglishArray)) * 100) # Calculates how many T's there are in array and outputs a % english
    cipherEnglishArray.clear()
    return clearScore

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

noFormatCipherText = input("enter ciphertext: ")
cipherText = noFormatCipherText.lower()
shifts = 0
cipherPermsArray = []
while shifts < 26: #tries every key
  cipherPerms = encrypt(cipherText, shifts)
  cipherPermsArray.append(cipherPerms)
  clearScore = clearScoreEnglish(cipherPermsArray[shifts])
  if clearScore > 30:
    print(clearScore, cipherPermsArray[shifts])
  shifts = shifts + 1
 
print("no Solutions")
