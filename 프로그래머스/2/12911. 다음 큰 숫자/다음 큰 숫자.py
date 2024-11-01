def solution(n):
    t_n=n
    n2=''
    while t_n!=0:
        n2=str(t_n%2)+n2
        t_n=int(t_n/2)
    n_len=len(n2)
    n_count=n2.count('1')
    res_i=n
    res2=list(n2)
    res2.reverse()
    while res_i==n or res2.count('1')!=n_count:
        res_i+=1
        for i in range(len(res2)):
            if res2[i]=='0':
                res2[i]='1'
                break
            else:
                res2[i]='0'
        if res2[-1]=='0':
            res2.append('1')
    return res_i