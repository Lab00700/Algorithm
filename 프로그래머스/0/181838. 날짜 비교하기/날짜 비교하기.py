def solution(date1, date2):
    answer = 0
    t1=int(''.join(map(str,date1)))
    t2=int(''.join(map(str,date2)))
    if t1<t2:
        answer=1
    return answer
