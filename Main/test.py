def cconvertToCHARACTER(textList): #Converts an list of ASCII equivalent numbers into an list of their ASCII equivalent characters
    index = 0
    while index < len(textList): #goes through each list index and turns it from ASCII number to Character
        textList[index] = chr(textList[index])
        index += 1
    return textList

def convertToCHARACTER(textList): #Converts an list of ASCII equivalent numbers into an list of their ASCII equivalent characters
    output = []
    for n in textList:
        output.append(ord(n))
    return output

x = convertToCHARACTER(["a","b","c","d"])
print(x)