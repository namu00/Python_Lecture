#Problem 08.py
import string

def solution(sentence):
    orgstr = (sentence.replace(" ","")).replace(".","")
    #공백 제거한 문자열에서 마침표를 삭제
    revstr = orgstr[::-1]
    if revstr == orgstr: return True
    else : return False

sentence1 = "never odd or even."
ret1 = solution(sentence1)

print("Soluteion: return value of the function is",ret1,".")

sentence2 = "palindrome"
ret2 = solution(sentence2)

print("Solution: return calue of the funciton is",ret2,".")