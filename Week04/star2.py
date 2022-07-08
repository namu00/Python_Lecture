line_max = 10
line = 0
for line in range(0,line_max):
    invert_count = line_max - line
    for invert_count in range(invert_count,0,-1):
        print(' ',end = '')
    star = line
    for star in range(0,2*line - 1):
        print('*',end = '')
    print("")
print("invert count : " , invert_count)