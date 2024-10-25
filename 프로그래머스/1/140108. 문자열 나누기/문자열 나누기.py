def solution(s):
    answer = 0
    first=''
    count=0
    diff_count=0
    for i in s:
        if first=='':
            first=i
            count=1
        elif first==i:
            count+=1
        else:
            diff_count+=1
        if count==diff_count:
            first=''
            count=0
            diff_count=0
            answer+=1
    if first!='':
        answer+=1
    return answer