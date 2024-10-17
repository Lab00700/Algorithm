def solution(numlist, n):
    down = []
    up = []
    answer = []
    for i in range(len(numlist)):
        numlist[i] -= n
        if numlist[i] < 0:
            down.append(0 - numlist[i])
        else:
            up.append(numlist[i])
    down.sort()
    up.sort()

    a = 0
    b = 0
    while a < len(down) or b < len(up):
        if a == len(down):
            answer.extend(map(lambda x:up[x]+n,range(b,len(up))))
            break
        if b == len(up):
            answer.extend(map(lambda x:0-down[x]+n,range(a,len(down))))
            break
        if down[a] < up[b]:
            answer.append(0 - down[a] + n)
            a += 1
        else:
            answer.append(up[b] + n)
            b += 1
        print(answer,a,b)
    return answer