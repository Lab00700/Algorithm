def solution(age):
    age = str(age)
    answer = ''
    for i in range(len(list(age))):
        answer += chr(ord('a') + int(age[i])) #a를 아스키 코드 값으로 변환하고 age[i] 값을 더한 후 문자로 다시 변환  

    return answer
