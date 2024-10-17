def solution(quiz):
    answer = []
    temp=[]
    for i in range(len(quiz)):
        q=quiz[i].split('=')
        ans=q[1].split()
        qq=q[0].split()
        t=int(qq[0])
        a=''
        for i in range(1,len(qq)):
            if qq[i]=='+':
                a='+'
            elif qq[i]=='-':
                a='-'
            else:
                if a=='+':
                    t+=int(qq[i])
                else:
                    t-=int(qq[i])
        if int(ans[0])==t:
            answer.append("O")
        else:
            answer.append("X")

    return answer