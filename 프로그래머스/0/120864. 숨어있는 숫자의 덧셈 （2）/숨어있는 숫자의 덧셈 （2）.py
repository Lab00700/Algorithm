def solution(my_string):
    answer = 0
    for i in range(26):
        my_string = my_string.replace(chr(ord('a') + i), ' ') #문자를 아스키코드로 변환 후 i를 더하고 다시 문자로 변환
        my_string = my_string.replace(chr(ord('A') + i), ' ')

    return sum(map(int,my_string.split()))
