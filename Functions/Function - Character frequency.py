def characterFrequency(encryptedText):
    frequencies=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    for i in encryptedText: #iterates through each character in encrypted_cipher text
        index = 0 #element index set at 0
        #WHEN data at index (character in encrypted text) does not equal first element
        #AND the alphabet index is less than 25, (i.e all letters encompassed only):
        while i != letter[index] and index < 25: #THEN increment pos index ++, avoids indexing greater than alphabet list
           if index <= 24:
               index = index + 1
        else: #increments relative index dependant upon character contained within i
            if i == letter[index]:
                frequencies[index] = frequencies[index]+1 #if character in encrypted_text is a space,data @ alphabet[26] ++:
            elif i == " ":
                 frequencies[26]= frequencies[26]+1 #if character in encrypted_text therefore is not a recognised characer,data @ alphabet[27] ++
            else:
                frequencies[27]= frequencies[27]+1              
    return frequencies