def solution(arr):
    revarr = []
    #reverse array
    for i in range(0,len(arr)):
        revarr.append(arr[-(i+1)])
    #list's indexing can support negative indexing.
    #list[last] = list[-1]
    return revarr
if __name__=="__main__":
    arr = [1,2,3,4]
    ret = solution(arr)
    
    print("Solution:return value of the function is ",ret,".")