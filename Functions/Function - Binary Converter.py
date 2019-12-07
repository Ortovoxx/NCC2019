import re
def BINtoDEC(binary):
    return int(str(binary),2)

def DECtoBIN(decimal):
    return int(re.sub("0b","",str(bin(decimal))))

x = BINtoDEC(1111110010100101)
y = DECtoBIN(64677)
print(x)
print(y)