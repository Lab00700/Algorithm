def solution(a, b, c):
    q=set({a,b,c})
    if len(q)==3:
        return a+b+c
    elif len(q)==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return a*3*(a**2)*3*(a**3)*3