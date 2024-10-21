def solution(phone_number):
    answer = "{0:*>{1}}".format(phone_number[-4:],len(phone_number))
    return answer