def solution(cipher, code):
    answer = ''
    for i in range(code-1,len(list(cipher)),code):
        answer+=cipher[i]
    return answer