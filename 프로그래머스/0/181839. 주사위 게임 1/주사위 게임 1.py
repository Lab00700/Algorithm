def solution(a, b):
    if (a+b)%2==0:
        if a%2==0:
            return a-b if a>b else b-a
        return a**2+b**2
    return (a+b)*2