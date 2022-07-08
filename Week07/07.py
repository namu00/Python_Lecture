def solution(scores):
    count = 0
    for i in range(0,len(scores)):
        if scores[i] >=650 and scores[i] < 800:
            count +=1
            
    return count
if __name__=="__main__":
    scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
    ret = solution(scores)
    
    print("Solution: return value of the fucntion is ",ret,".")