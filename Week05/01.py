def solution(price,grade):
    discnt = 0 #할인율
    if grade == "S": discnt = 0.05
    elif grade == "G": discnt = 0.1
    else : discnt = 0.15
    answer = int(discnt*float(price))
    return answer

if __name__=="__main__":    
    price1 = 2500
    grade1 = "V"    
    ret1 = solution(price1,grade1)

    print("Solution:return value of the function is",ret1,".")
    print("When you are \""+grade1+"\" grade, And you purchased product pricing 2500,")
    print("Total charge is ",price1,"-",ret1,"=",price1-ret1)

    price2 = 96900
    grade2 = "S"
    ret2 = solution(price2,grade2)

    print("solution:return value of the function is",ret2,".")
    print("When you are \""+grade2+"\" grade, And you purchased product pricing",price2,",")
    print("Total charge is ",price2,"-",ret2,"=",price2-ret2)
