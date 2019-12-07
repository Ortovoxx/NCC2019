import re
def BINtoDEC(binary):
    return int(str(binary),2)

def DECtoBIN(decimal):
    return int(re.sub("0b","",str(bin(decimal))))

def DECtoHEX(decimal):
    return re.sub("0x","",str(hex(decimal)))

def HEXtoDEC(hexN):
    return int(str(hexN),16)

x = BINtoDEC(1111110010100101)
y = DECtoBIN(64677)
z = DECtoHEX(255)
a = HEXtoDEC("ff")
print(x)
print(y)
print(z)
print(a)