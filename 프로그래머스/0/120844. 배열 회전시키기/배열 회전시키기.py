def solution(numbers, direction):
    answer = []
    if direction=='right':
        numbers.insert(0,numbers[-1])
        del numbers[-1]
    elif direction=='left':
        numbers.append(numbers[0])
        del numbers[0]
    answer=numbers
    return answer