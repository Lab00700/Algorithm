def solution(answers):
    a1=[1,2,3,4,5]
    a2=[2,1,2,3,2,4,2,5]
    a3=[3,3,1,1,2,2,4,4,5,5]
    a=[a1,a2,a3]
    s=[0,0,0]
    answer=[]
    for i in range(len(answers)):
        for k in range(3):
            if answers[i]==a[k][i%len(a[k])]:
                s[k]+=1
    for i in range(3):
        if s[i] == max(s):
            answer.append(i + 1)
    return answer