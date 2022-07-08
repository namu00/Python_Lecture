def solution(arr):
    number_count = [0]*max(arr)
    for i in range(0,max(arr)+1):
        count = arr.count(i)
        number_count.insert(i,count)
    #number_count[num] -> count of num in arr
    cnt = max(number_count)//minimum(number_count)
    return cnt

def minimum(arg):
#minimum except 0
    ret = []
    for i in range(0,len(arg)):
        if arg[i] != 0:
            ret.append(arg[i])
    return min(ret)

if __name__=="__main__":
    arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
    print(arr.count(3))
    ret = solution(arr)
#Press Run button to receive output.
    print("Solution: return value of the function is", ret, ".")