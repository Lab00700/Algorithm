def solution(numbers, hand):
    answer = ''
    if hand == "right":
        hand = 1
    else:
        hand = 0
    l = [1, 3]
    r = [1, 3]
    left = [1, 4, 7, '*']
    middle = [2, 5, 8, 0]
    right = [3, 6, 9, '#']

    for n in numbers:
        if n in left:
            answer += 'L'
            l = [1, left.index(n)]
        elif n in right:
            answer += 'R'
            r = [1, right.index(n)]
        else:
            m_index = middle.index(n)
            l_val = m_index - l[1]
            r_val = m_index - r[1]
            if l_val < 0:
                l_val = 0 - l_val
            if r_val < 0:
                r_val = 0 - r_val
            l_val += l[0]
            r_val += r[0]
            if l_val < r_val or (l_val == r_val and not hand):
                answer += 'L'
                l = [0, m_index]
            elif r_val < l_val or (l_val == r_val and hand):
                answer += 'R'
                r = [0, m_index]

    return answer