#Problem 10.py
def solution(data):
    cnt = 0
    
    for i in range(0,len(data)):
        if data[i] < (lambda data : sum(data)/len(data))(data) : cnt += 1
        #메모리 관점에서 이득
        #프로세스 관점에서 손해
    return cnt

data1 = [1,2,3,4,5,6,7,8,9,10]
ret1 = solution(data1)

print("Solution: return value of the unction is", ret1,".")

data2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
ret2 = solution(data2)

print("Solution: return value of the function is", ret2,".")