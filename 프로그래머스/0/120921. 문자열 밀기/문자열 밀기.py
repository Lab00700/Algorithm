def find(t1,t2,i):
    t2=''.join(t2[i:])+''.join(t2[:i])
    if t1==t2:
        return i
    return -1

def solution(A, B):
    answer = -1
    t1=A
    t2=list(B)
    for i in range(len(t2)):
        if t1[0]==t2[i]:
            answer=find(t1,t2,i)
            if answer!=-1:
                break
    return answer