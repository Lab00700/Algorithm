def solution(s):
    answer=0
    start=0
    end=len(s)-1
    s=s+s
    while end<len(s)-1:
        stack=[]
        i=start
        while i<=end:
            if not stack and (s[i]=="}" or s[i]==")" or s[i]=="]"):
                stack.append(None)
                break
            if s[i]=="{" or s[i]=="(" or s[i]=="[":
                stack.append(s[i])
            else:
                if s[i]=="}" and stack[-1]=="{":
                    stack.pop()
                elif s[i]==")" and stack[-1]=="(":
                    stack.pop()
                elif s[i]=="]" and stack[-1]=="[":
                    stack.pop()
                else:
                    break
            i+=1
        if not stack:
            answer+=1
        start+=1
        end+=1
    return answer