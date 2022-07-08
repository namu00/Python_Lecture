import os
filename = "./notepad.txt"

if os.path.exists(filename):
    print("file exist") 
else:
    print("file not found")

f = open(filename, 'r', encoding='UTF-8')
# while True:
#     linedata = f.readline()
#     if linedata == '':
#         break;
#     linedata = linedata.rstrip('\n')
#     print(linedata) 
data = f.readlines()
print(data)

f.close()