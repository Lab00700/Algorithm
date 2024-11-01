def solution(A,B):
    answer=0
    A.sort()
    B.sort()
    while A or B:
        if A[-1]*B[0]<B[-1]*A[0]:
            answer+=A[-1]*B[0]
            A.pop(-1)
            B.pop(0)
        else:
            answer+=A[0]*B[-1]
            A.pop(0)
            B.pop(-1)
    return answer