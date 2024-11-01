def solution(s):
    stack=[]
    for k in s:
        stack.append(k)
        if len(stack)>1 and stack[-1]==stack[-2]:
            stack.pop()
            stack.pop()
    if stack:
        return 0
    return 1