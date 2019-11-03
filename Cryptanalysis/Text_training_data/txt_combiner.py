import os

os.chdir("/Users/Euan/Desktop/NCC2019/Cryptanalysis/Text_training_data/training_text")
fileNames = os.listdir("/Users/Euan/Desktop/NCC2019/Cryptanalysis/Text_training_data/training_text")
with open("training_text_output.txt", "w") as outputFile:
    for name in fileNames:
        with open(name, "r") as inputFile:
            for line in inputFile:
                outputFile.write(line)

'''
x = os.listdir("/Users/Euan/Desktop/NCC2019/Cryptanalysis/Text_training_data/training_text")
y = len(x)
print(y)
#get rid of 30
#1000


#*** START OF THIS PROJECT GUTENBERG EBOOK XXX ***
#**The Project Gutenberg Etext XXX**


#*** END OF THIS PROJECT GUTENBERG EBOOK XXX ***


os.chdir("/Users/Euan/Desktop/NCC2019/Cryptanalysis/Text_training_data/test")
fileNames = os.listdir("/Users/Euan/Desktop/NCC2019/Cryptanalysis/Text_training_data/test")
with open("training_text_output.txt", "w") as outputFile:
    for name in fileNames:
        with open(name, "r") as inputFile:
            data  = inputFile.read()
            dataArray = list(data)
            index = 0
            while index < len(dataArray):
                print("workiung")
                if dataArray[index] and dataArray[index + 1] and dataArray[index + 2] == "*":
                    print(dataArray[index])
                    dataindex = 0
                    while dataindex < index:
                        dataArray.pop(dataindex)
                        dataindex = dataindex + 1
                if dataArray[index] and dataArray[index + 1] and dataArray[index + 2] == "*":
                    #print(index)
                    dataindexend = 0
                    while dataindexend < index:
                        dataArray.pop(dataindexend)
                        dataindexend = dataindexend + 1
                #print(index)
                index = index + 1
        with open(name, "w") as f:
            print("te")
            newdata = "".join(dataArray)
            f.writelines(newdata)


os.chdir("/Users/Euan/Desktop/NCC2019/Cryptanalysis/Text_training_data/test")
fileNames = os.listdir("/Users/Euan/Desktop/NCC2019/Cryptanalysis/Text_training_data/test")
with open("training_text_output.txt", "w") as outputFile:
    for name in fileNames:
        with open(name, "r") as f:
            lines = f.readlines()
        with open(name, "w") as f:
            for line in lines:
                if line.strip("\n") != "title":
                    f.write(line)


os.chdir("/Users/Euan/Desktop/NCC2019/Cryptanalysis/Text_training_data/test")
with open("training_text33.txt", "r") as f:
    lines = f.readlines()
with open("training_text33.txt", "w") as f:
    for line in lines:
        linearray = list(lines)
        if line.strip("\n") != "Title":
            f.write(line)
            '''