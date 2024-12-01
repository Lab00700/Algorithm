def solution(word):
    answer = 0
    dic_digit={ #자릿수 별 경우의 수
        0:781,
        1:156,
        2:31,
        3:6,
        4:1
    }
    dic_word={ #모음 별 더하는 수
        'A':0,
        'E':1,
        'I':2,
        'O':3,
        'U':4
    }
    i=0
    for w in word:
        answer+=dic_word[w]*dic_digit[i]+1 #자릿수값, 모음값 곱셈 후 1 더하기(A를 고려)
        i+=1 #다음 자리
    return answer