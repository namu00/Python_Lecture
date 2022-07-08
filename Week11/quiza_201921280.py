def solution(arr):
    m3count = 0
    m5count = 0
    for i in range(0,len(arr)):
        if(arr[i] % 3 == 0): m3count +=1
        if(arr[i] % 5 == 0): m5count +=1

    if m3count > m5count: answer = 'three'
    elif m5count > m3count : answer = 'five'
    else : answer = 'same'
    return answer

arr = [2, 3, 6, 9, 12, 15, 10, 20, 22, 25]
ret = solution(arr)
print("solution is ", ret, ".")