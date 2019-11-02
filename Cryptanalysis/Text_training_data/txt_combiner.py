import os

os.chdir("/Users/Euan/Desktop/NCC2019/Cryptanalysis/Text_training_data/training_text")
fileNames = os.listdir("/Users/Euan/Desktop/NCC2019/Cryptanalysis/Text_training_data/training_text")
with open("training_text.txt", "w") as outputFile:
    for name in fileNames:
        with open(name, "r") as inputFile:
            for line in inputFile:
                outputFile.write(line)


