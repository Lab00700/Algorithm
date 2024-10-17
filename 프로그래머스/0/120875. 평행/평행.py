def sol(a, b): #기울기 구하기
    x = a[0] - b[0]
    y = a[1] - b[1]
    return x / y

def solution(dots):
    answer = 0
    for i in range(len(dots)):
        for k in range(i + 1, len(dots)):
            temp=dots.copy() #배열 복사
            t1 = sol(temp[i], temp[k]) #선택한 두 점 기울기 구하기
            del temp[k] #선택한 두 점 배제
            del temp[i]
            t2 = sol(temp[0],temp[1]) # 나머지 두 점 기울기 구하기
            if t1==t2: #기울기 같으면 두 직선이 평행
                return 1

    return answer