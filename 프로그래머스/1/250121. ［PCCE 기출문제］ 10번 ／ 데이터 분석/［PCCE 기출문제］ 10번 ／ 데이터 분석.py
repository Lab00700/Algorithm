def solution(data, ext, val_ext, sort_by):
    answer=[]
    if sort_by=="code":
        s=0
    elif sort_by=="date":
        s=1
    elif sort_by=="maximum":
        s=2
    else:
        s=3
    if ext=="code":
        e=0
    elif ext=="date":
        e=1
    elif ext=="maximum":
        e=2
    else:
        e=3
    for d in data:
        if d[e]<val_ext:
            answer.append(d)
    answer=sorted(answer,key=lambda x:x[s])
    return answer