def solution(numbers, target):
    def cal(s,i):
        if i==len(numbers):
            if s==target: #모든 숫자를 계산했을 때 값이 target이면 return 1
                return 1
            return 0 #아니라면 return 0
        res=cal(s+numbers[i],i+1) #더하는 경우
        res+=cal(s-numbers[i],i+1) #빼는 경우
        return res
    answer = cal(0,0)
    return answer