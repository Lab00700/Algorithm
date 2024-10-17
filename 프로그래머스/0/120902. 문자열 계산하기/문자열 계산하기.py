def solution(my_string):
    a=my_string.split()
    answer = int(a[0])
    b=''
    for i in range(1,len(a)):
        if a[i]=='+' or a[i]=='-':
            b=a[i]
        else:
            val=int(a[i])
            if b=='-':
                answer-=val
            else:
                answer+=val
    return answer