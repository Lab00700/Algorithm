def solution(s):
    a = []
    for i in range(len(list(s))):
        if s[i] == "(":
            a.append("(") #괄호 열림 저장
        else:
            if len(a)==0: #괄호 열린 것이 없는데 괄호 닫힘이 오면 return False
                return False
            else: #괄호 닫힘이 오면 pop
                a.pop()
    if len(a)!=0: #배열 a 안에 요소가 남아있으면 제대로 닫히지 않았으므로 return False
        return False
    return True