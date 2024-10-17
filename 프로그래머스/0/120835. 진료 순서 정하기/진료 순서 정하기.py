def solution(emergency):
    t=[]
    for i in range(len(emergency)):
        t.append(0)
    for i in range(len(emergency)):
        t[emergency.index(max(emergency))]=i+1 #위급한 순서로 진료 순서 지정
        emergency[emergency.index(max(emergency))]=0 #순서 정한 값 0으로 저장하여 max로 불러와지지 않도록 함
    
    return t
