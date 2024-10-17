def solution(array, n):
    temp=array.copy()
    for i in range(len(array)):
        array[i]=n-array[i] if n>array[i] else array[i]-n
    q=list(filter(lambda  x: array[x]==min(array),range(len(array))))
    answer = min(map(lambda x: temp[x], q))
    return answer