def solution(arr, k):
    answer = list(map(lambda x:arr[x]*k if k%2!=0 else arr[x]+k,
                      range(len(arr))))
    return answer