def solution(arr):
    arr.remove(min(arr))
    if not len(arr):
        arr.append(-1)
    return arr