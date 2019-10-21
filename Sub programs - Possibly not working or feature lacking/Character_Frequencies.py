def character_frequency(encrpyted_text):

    #2D array consisting of alphabet: ["letter",no. of lowercase instances, no. of uppercase instances]
    #alphabet[26][1]: number of spaces
    #aplhabet[26][2]: number of unknown characters
    
    alphabet=[["a",0,0],["b",0,0],["c",0,0],["d",0,0],["e",0,0],["f",0,0],["g",0,0],["h",0,0],["i",0,0],["j",0,0],["k",0,0],["l",0,0],["m",0,0],["n",0,0],["o",0,0],["p",0,0],["q",0,0],["r",0,0],["s",0,0],["t",0,0],["u",0,0],["v",0,0],["w",0,0],["x",0,0],["y",0,0],["z",0,0],["space_or_unknown_char",0,0]]

    """encrpyted_text= input("enter cipher text")"""#TESTING PURPOSES ONLY


    #iterates through each character in encrypted_cipher text
    for i in encrpyted_text:
        letter = 0 #element index set at 0





        #WHEN data at index (character in encrypted text) does not equal first element in alphabet (i.e "a" or "A")
        #AND the alphabet index is less than 25, (i.e all letters encompassed only:
        
        while i != alphabet[letter][0].upper() and i != alphabet[letter][0] and letter < 25:
            """print(alphabet[letter][0])"""#TESTING PURPOSES ONLY
        #THEN increment pos index ++, avoids indexing greater than alphabet list
            if letter <= 24:
               letter = letter + 1
        #ELSE
        else:
        #Already know, at this point, that character in encrypted_text is a letter - now deciding as to wether it is in form upper or lower case
        #if character in encrypted_text is equal to CAPITALISED letter ++ pos[1] in alphabet[element]
            if i == alphabet[letter][0].upper():
                alphabet[letter][2] = alphabet[letter][2]+1
        #if character in encrypted_text is equal to CAPITALISED letter ++ pos[2] in alphabet[element]
            elif i == alphabet[letter][0]:
                alphabet[letter][1] = alphabet[letter][1]+1
        #If character in encrypted_text is not equal to upper or lower letter (stated within the aplahabet list - indicated by element range)
        #if character in encrypted_text therefore is a space, then ++ last element in alphabet pos 1(alphabet[26][1]) 
            elif i== " ":
                alphabet[26][1] = alphabet[26][1]+1
        #if character in encrypted_text therefore is not a recognised characer, then ++ last element in alphabet pos 2(alphabet[26][2]) 
            else:
                alphabet[26][2] = alphabet[26][2]+1
                        

    """print(alphabet)"""#TESTING PURPOSES ONLY
    #Displays number of each LOWERcase letter found in enrcypted_text
    for i in alphabet[0:26]:
        print(i[0],"=", i[1])
    print("\n")
    #Displays number of each UPPERcase letter found in enrcypted_text
    for i in alphabet[0:26]:
        print(i[0].upper(),"=", i[2])
    #Displays number of SPACES found in enrcypted_text
    print("Spaces =",alphabet[26][1])
    #Displays number of each UNKNOWN CHARACTERS found in enrcypted_text

    # due to nature fo this code, numbers will be classified as unknown characters -
    #I'm currently writing code which can work in conjunction with this code to rectify this
    #Did not want to add it to this stage in case it causes a tonne of bugs - so I will place revised version on discord in a few days


    
    print("Unknown characters =", alphabet[26][2])

"""user = str(input("enter cipher text"))"""#TESTING PURPOSES ONLY
"""character_frequency(user)"""#TESTING PURPOSES ONLY
