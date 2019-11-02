import time
import requests
import os

#"http://www.gutenberg.org/files/" + str(index) + "/" + str(index) + ".txt" <<<<<< ASCII ENCODING
#"http://www.gutenberg.org/files/" + str(index) + "/" + str(index) + "-0.txt" <<<<< GIVES UTF-8 ENCODING

os.chdir("/Users/Euan/Desktop/NCC2019/Cryptanalysis/Text_training_data/training_text")
index = 1
while index < 5000:
    url = "http://www.gutenberg.org/files/" + str(index) + "/" + str(index) + ".txt"
    myfile = requests.get(url)
    filename = "training_text" + str(index) + ".txt"
    remove = False
    with open(filename,"ab") as f: 
        f.write(myfile.content)
    with open(filename,"r") as f:
        dataUnformatted = f.read()
        quadramData = list(dataUnformatted)
        if quadramData[0] == "<":
            remove = True
    if remove == True:
        os.remove(filename)
    time.sleep(1)
    index = index + 1


