'''
Allows scoring of text using n-gram probabilities
17/07/12

from math import log10

# 389,373 unique quadrams in the file



class ngram_score(object):
    def __init__(self,ngramfile,sep=' '):
        # load a file containing ngrams and counts, calculate log probabilities 
        self.ngrams = {}
        for line in file(ngramfile):
            key,count = line.split(sep) 
            self.ngrams[key] = int(count)
        self.L = len(key)
        self.N = sum(self.ngrams.itervalues())
        #calculate log probabilities
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)
        self.floor = log10(0.01/self.N)

    def score(self,text):
        # compute the score of text 
        score = 0
        ngrams = self.ngrams.__getitem__
        for i in xrange(len(text)-self.L+1):
            if text[i:i+self.L] in self.ngrams: score += ngrams(text[i:i+self.L])
            else: score += self.floor          
        return score

'''
import os






os.chdir("/Users/Euan/Desktop/NCC2019/Cryptanalysis/ngrams")
x = os.getcwd() #current working directory
y = os.listdir() #lists all items in a directory


#print(y)
#print(x)

quadramDitionaryCiphertext = {}


quadramDitionaryEnglish = {}
index = 0
with open("english_quadgrams.txt", "r") as f:
    quadramData = f.read()
    quadramArray = quadramData.split()
    while index < len(quadramArray):
        quadramDitionaryEnglish[quadramArray[index]] = int(quadramArray[index + 1])
        index = index + 2
    #print(quadramDitionaryEnglish)


print("done")