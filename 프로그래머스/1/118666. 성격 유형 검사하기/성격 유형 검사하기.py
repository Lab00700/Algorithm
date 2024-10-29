def solution(survey, choices):
    answer = ''
    a=0
    b=0
    c=0
    d=0
    for i in range(len(survey)):
        t1,_=survey[i]
        choices[i]-=4
        if 'R' in survey[i]:
            if t1=='R':
                a-=choices[i]
            else:
                a+=choices[i]
        elif 'C' in survey[i]:
            if t1=='C':
                b-=choices[i]
            else:
                b+=choices[i]
        elif 'J' in survey[i]:
            if t1=='J':
                c-=choices[i]
            else:
                c+=choices[i]
        elif 'A' in survey[i]:
            if t1=='A':
                d-=choices[i]
            else:
                d+=choices[i]
    answer+='T' if a<0 else 'R'
    answer+='F' if b<0 else 'C'
    answer+='M' if c<0 else 'J'
    answer+='N' if d<0 else 'A'
    return answer