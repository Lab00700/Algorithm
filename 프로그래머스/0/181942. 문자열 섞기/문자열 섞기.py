def solution(str1, str2):
    i=0
    answer = ''
    str1=list(str1)
    str2=list(str2)
    while i<(len(str1) if len(str1)>len(str2) else len(str2)):
        if i<len(str1):
            answer+=str1[i]
        if i<len(str2):
            answer+=str2[i]
        i+=1
    return answer