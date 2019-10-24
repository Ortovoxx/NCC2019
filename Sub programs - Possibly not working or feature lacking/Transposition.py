#columnar transposition cipher
ciphertext = input("CipherText: ")
ciphertextlength = len(ciphertext)
ciphertextarray = list(ciphertext)
print(ciphertextarray)
#gets the number of columns used in the transposition P.s make sure that the ciphertextlength is exactly divisible by the columnumber. If not u can always add a few random characters to even it out.
columnnumber = int(input("number of columns"))
# creates the same number of arrays as columns
columns = [[" "] for j in range (0,columnnumber)] 
columnlength = int(ciphertextlength/columnnumber)
i = 0
j = 0
# splits the ciphertext into columns and iterates through until no more letters are left
while j < columnnumber and i < ciphertextlength:
  columns[j] = [ciphertextarray[i:columnlength]]
  j += 1
  i = i + columnlength
  columnlength = columnlength + columnlength
print(columns)


#rearrange the ciphertext until it is plaintext?