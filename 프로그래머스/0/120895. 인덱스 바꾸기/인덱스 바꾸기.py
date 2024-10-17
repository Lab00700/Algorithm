def solution(my_string, num1, num2):
    answer = list(my_string)
    answer.insert(num1,answer[num2])
    answer.insert(num2+1,answer[num1+1])
    del answer[num1+1]
    del answer[num2+1]
    
    return ''.join(answer)