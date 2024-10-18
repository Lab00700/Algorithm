def solution(arr, delete_list):
    a=set(arr)
    b=set(delete_list)
    a=a.intersection(b)
    for i in a:
        arr.remove(i)
    return arr