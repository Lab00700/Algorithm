def solution(n):
    answer = 0
    x=n
    y=0
    while x>=0:
        result=1
        if x>y:
            a,b=x,y
        else:
            a,b=y,x
        b_list=[]
        for i in range(2,b+1):
            b_list.append(i)
        for i in range(a+1,a+b+1):
            result*=i
            b_i=0
            while b_i<len(b_list):
                if result%b_list[b_i]==0:
                    result//=b_list[b_i]
                    b_list.pop(b_i)
                    break
                b_i+=1
            if not b_list:
                result %= 1234567
        print(x,y,result)
        x-=2
        y+=1
        answer+=result
        answer%=1234567
    return answer