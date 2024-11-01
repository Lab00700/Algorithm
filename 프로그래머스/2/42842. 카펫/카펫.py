def solution(brown, yellow):
    y=[]
    for i in range(1,yellow+1):
        if yellow%i==0:
            if (yellow/i+i)*2+4==brown:
                return [yellow/i+2,i+2]