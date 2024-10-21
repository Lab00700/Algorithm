def solution(l, r):
    answer = []
    a = ['5']
    t = 5
    while t <= r:
        if t>=l:
            answer.append(t)
        if a[0] == '5':
            for i in range(0, len(a)):
                if a[i] == '5':
                    a[i] = '0'
                    if i == len(a) - 1:
                        a.append('5')
                else:
                    a[i] = '5'
                    break
        else:
            a[0] = '5'
        a.reverse()
        t = int(''.join(a))
        a.reverse()
    if len(answer)==0:
        answer.append(-1)
    return answer