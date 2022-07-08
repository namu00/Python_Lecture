def solution(number):
    count = 0
    num2str = []
    #number list but, in str 
    for i in range(1,number+1):
        num2str.append(i)
    num2str = str(num2str)
    #append str type number to num2str list
    count += num2str.count('3')
    count += num2str.count('6')
    count += num2str.count('9')
    #counting number of 3, 6, 9 in num2str list 
    return count

if __name__ == "__main__":
    number = 40
    ret = solution(number)
    
    print("solution: return value of the funciton is ",ret,".")