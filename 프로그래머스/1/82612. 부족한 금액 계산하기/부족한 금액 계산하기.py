def solution(price, money, count):
    answer=sum(map(lambda x:x*price,range(count+1)))-money
    if answer<0:
        return 0
    return answer