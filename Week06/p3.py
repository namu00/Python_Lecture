def solution(start_month, start_day, end_month, end_day):
    start = get_jan2d(start_month,start_day)
    end = get_jan2d(end_month,end_day)
    day = end - start
    return day


def get_jan2d(m,d):
    #return How many days passed since January 1st.
    day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #total days from January to December
    #index 0 -> total days of January
    #index LAST -> total days of December
    day = 0
    for i in range(0,(m-1)):
        day += day_list[i]
    return (day+d)

if __name__ == "__main__":
    start_month = 1
    start_day = 2
    end_month = 3
    end_day = 2
    ret = solution(start_month, start_day, end_month, end_day)
    
    print("Solution: return value of the func is ",ret,".")