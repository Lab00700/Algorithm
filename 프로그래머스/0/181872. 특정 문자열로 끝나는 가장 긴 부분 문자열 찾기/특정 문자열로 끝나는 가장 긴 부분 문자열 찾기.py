def solution(myString, pat):
    answer = myString.split(pat)
    answer.pop()
    answer=pat.join(answer)+pat
    return answer