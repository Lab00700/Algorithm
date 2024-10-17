def solution(num_list):
    answer = 0
    a=1
    for i in range(len(num_list)):
        a*=num_list[i] #모든 수의 곱
    if a<sum(num_list)**2: #모든 수의 합의 제곱과 모든 수의 곱 비교
        answer=1

    return answer