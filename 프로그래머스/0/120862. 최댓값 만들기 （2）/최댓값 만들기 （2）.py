def solution(numbers):
    pt=numbers.copy() #양수 곱 최대값
    p = max(pt)
    del pt[pt.index(p)]
    p *= max(pt)

    mt = numbers.copy() #음수 곱 최대값
    m = min(mt)
    del mt[mt.index(m)]
    m *= min(mt)
    answer = p if p > m else m
    return answer
