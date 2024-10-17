def solution(arr):
    answer = []
    answer.append(arr[0]) #arr 배열의 첫 번째 값 추가
    k=arr[0] #초기 비교 값 저장
    for i in range(1,len(arr)):
        if k!=arr[i]: #비교 값 다르면 새로운 값
            answer.append(arr[i]) #새로운 값 추가
            k=arr[i] #비교 값 갱신
    
    return answer
