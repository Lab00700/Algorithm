def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer1 *= denom2
    numer2 *= denom1
    denom = denom1 * denom2
    numer = numer1 + numer2

    i = 2
    while i <= (numer if numer < denom else denom): #기약 분수로 변환
        if numer % i == 0 and denom % i == 0:
            numer /= i
            denom /= i
        else:
            i += 1

    answer.append(int(numer))
    answer.append(int(denom))


    return answer
