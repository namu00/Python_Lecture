def solution(shirt_size):
    size = [0]*6
    #count of size sx, s, m, l, xl, xxl
    #index 0 -> count of size "SX"
    #index LAST -> count of size "XXL"
    answer = []
    for i in range(0,len(shirt_size)):
        if shirt_size[i] == "XS" : size[0] += 1
        elif shirt_size[i] == "S" : size[1] += 1
        elif shirt_size[i] == "M" : size[2] += 1
        elif shirt_size[i] == "L" : size[3] += 1
        elif shirt_size[i] == "XL" : size[4] +=1
        else : size[5] += 1
    for i in range(0,len(shirt_size)):
        answer.append(size[i])
    return answer

if __name__=="__main__":
    shirt_size = ["XS","S","L","L","XL","S"]
    ret = solution(shirt_size)
    len(ret)
    print("Solution: return value of the func is ",ret,".")