file = "./notepad.txt"
key = 100

def encryption():
    f1 = open(file,'r',encoding = 'UTF-8')
    f2 = open("encrypted.txt",'w',encoding = 'UTF-8')
    outstr = ""
    
    while True:
        data = f1.readline()
        if data == "":
            break;
        
        for i in range (0,len(data)):
            ch = data[i]
            numch = ord(ch)
            numch += key
            ch2 = chr(numch)
            outstr = outstr + ch2
        f2.write(outstr)
        outstr = ""
    f1.close()
    f2.close()
        
def decryption():
    f1 = open("encrypted.txt",'r',encoding = 'UTF-8')
    f2 = open("decrypted.txt",'w',encoding = 'UTF-8')
    outstr = ""
    while True:
        data = f1.readline()
        if data == "":
            break;
        
        for i in range(0,len(data)):
            ch = data[i]
            numch = ord(ch)
            numch -= key
            ch2 = chr(numch)
            outstr = outstr + ch2
        f2.write(outstr)
        outstr = ""
    f1.close()
    f2.close()
            
    
if  __name__ == "__main__":
    encryption()
    decryption()