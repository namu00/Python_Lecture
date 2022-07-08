#Probelm 09.py
def solution(characters):
    result = "" + characters[0]
    for i in range(0,len(characters)):
        if i == 0: continue
        if characters[i-1] == characters[i] : continue
        result += characters[i]
    return result

characters = "senteeeencccccceeee"
ret = solution(characters)

print("Solution: return value of the function is", ret, ".")