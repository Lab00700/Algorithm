def solution(nums):
    answer = 0
    s=set(nums)
    g=len(nums)/2
    if len(s)>=g:
        answer=g
    else:
        answer=len(s)
    return answer