import time
import requests
import os

#"http://www.gutenberg.org/files/" + str(index) + "/" + str(index) + ".txt" <<<<<< ASCII ENCODING 
# [ http://www.gutenberg.org/files/123/123.txt ]
#"http://www.gutenberg.org/files/" + str(index) + "/" + str(index) + "-0.txt" <<<<< GIVES UTF-8 ENCODING 
# [ http://www.gutenberg.org/files/123/123-0.txt ]

os.chdir("/Users/Euan/Desktop/NCC2019/Cryptanalysis/Text_training_data/training_text") #Directory you want files to be saved in
index = 1
while index < 44000:
    url = "http://www.gutenberg.org/files/" + str(index) + "/" + str(index) + ".txt" #constructs the .txt files url <<<<<< ASCII ENCODING
    myfile = requests.get(url) #downloads the file
    filename = "training_text" + str(index) + ".txt" #constructs file name
    remove = False
    with open(filename,"wb") as f: #makes or overwrites a new file and saves file
        f.write(myfile.content)
    with open(filename,"r") as f: #opens the newly written file and reads it
        dataUnformatted = f.read() 
        quadramData = list(dataUnformatted) # converts the file to an array
        if quadramData[0] == "<": #if the first character is a < (for <!DOCTYPE html) meaning there was a 404 file not found error
            remove = True
    if remove == True: #removes the file if there was a 404 error and therefore the file is just html
        os.remove(filename)
    time.sleep(1) #waits a second so gutenberg servers do not kick us off for downloading too quickly
    index = index + 1