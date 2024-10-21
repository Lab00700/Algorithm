def solution(strArr):
    dic={}
    for i in strArr:
        if len(i) in dic:
            dic[len(i)]+=1
        else:
            dic[len(i)]=1
    max=0
    for i in dic:
        if dic[i]>max:
            max=dic[i]
    return max