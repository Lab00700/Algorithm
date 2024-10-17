def check1(t): #3의 배수인지
    if t % 3 == 0:
        return 1
    return 0
def check2(t): #3을 포함하는지
    if '3' in list(str(t)):
        return 1
    return 0

def solution(n):
    t=0
    for i in range(n):
        t += 1
        while check1(t) or check2(t):
            if check2(t):
                q = list(str(t))
                for k in range(q.count('3')):
                    q[q.index('3')] = '4'
                t = int(''.join(q))
            if check1(t):
                t += 1
    answer=t
    return answer
