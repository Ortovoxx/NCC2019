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
'''
import textManipulation as tx
import Monoalphabetic as m
import Transposition as t
import Polyalphabetic as p
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
#                                                       Main command line functions
#==============================================================================================================================================================

def help():
    print('''
------------[CIPHER COMMAND HELP]-------------

-- General useage commands

    start // Starts solving
    cipher.style [cipher type] // Used to change the style of cipher between the 3 main types
        > cipher.style monoalphabetic
    

-- Monoalphabetic commands

    mono.solve [cipher solving method] // Selects between the different monoalphabetic cipher types
    

-- Transposition commands

-- Polyalphabetic commands

-- Input and output commands

    io.createOutput [output file name] // Creates a new text output file 
    io.createInput [input file name] // Creates a new text input file
    io.outputType [output structure type] // Sets the output type between: plain, JSON, array, [JSON output field]ONLY
        > io.outputType JSON
        > io.outputType keyONLY
    io.deleteFile [i/o file name] // Deletes a specific i/o file

-- Technical commands

-- Config commands

----------------------------------------------''')
    

def mainInput(): # returns a list with all the input commands
    inp = str(input("> ")).split()
    if len(inp) < 2:
        print("Please be more specific\nType 'help' for a list of commands")
        mainInput()
    return inp
    
    

def inputSmoothing(inp):
    if inp != str:
        print("no")

print("Cipher Challenge command interface version 1")
while 1:
    inp = mainInput()

    if inp[0] == "cipher.style":
        if inp[1] == "monoalphabetic":
            print("Cipher style change to monoalphabetic")
        if inp[1] == "transposition":
            print("Cipher style change to transposition")
        if inp[1] == "polyalphabetic":
            print("Cipher style change to polyalphabetic")
    elif 1 == 2:
        pass
