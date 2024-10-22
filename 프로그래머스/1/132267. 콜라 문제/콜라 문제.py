def solution(a, b, n):
    answer = 0
    while n>=a:
        answer+=int(n/a)*b
        n=n%a+int(n/a)*b
    return answer