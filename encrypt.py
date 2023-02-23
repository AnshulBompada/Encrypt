import random
import math



def CreateCode():
    listofimpnumbers = []
    i = 0
    x = 0
    y = 0 
    while(i < 9):
        y = x
        x = random.randrange(1, 100000000)
        while(y == x):
            x = random.randrange(1, 1000000000)
        listofimpnumbers.insert(i, x)
        i += 1
    return listofimpnumbers

def cantorNumberCreation():
    numberlist = CreateCode()
    number = 0
    i = 0
    while(i < 9):
        strvalue = str(math.sqrt(numberlist[i]))
        if(strvalue[i] == "."):
            flvalue == int(strvalue[i+1])
        if(strvalue[i] != "."):
            flvalue = int(strvalue[i])
        if(strvalue == "9"):
            flvalue -= 1
        if(strvalue != "9"):
            flvalue += 1
        number += float(flvalue)/(pow(10, -i))
        i += 1
    return number

z = cantorNumberCreation()

def encrypt(message, z):
    mid =  z * int(message)
    encmsg = str(mid)
    return encmsg

def decrypt(msg, z):
    mid = float(msg)/z
    dncmsg = str(mid)
    return dncmsg

print(decrypt(encrypt("6", z), z))