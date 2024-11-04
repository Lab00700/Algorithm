def solution(n, left, right):
    answer = []
    i=left
    while i<=right:
        i1=int(i/n)+1
        i2=i%n+1
        answer.append(i1 if i1>i2 else i2)
        i+=1
    return answer