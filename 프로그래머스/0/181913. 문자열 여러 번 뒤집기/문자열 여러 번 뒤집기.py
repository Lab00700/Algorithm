def solution(my_string, queries):
    my_string=list(my_string)
    for a,b in queries:
        t=my_string[a:b+1]
        t.reverse()
        q1=my_string[:a]
        q2=my_string[b+1:]
        q1.extend(t)
        q1.extend(q2)
        my_string=q1.copy()
    return ''.join(my_string)