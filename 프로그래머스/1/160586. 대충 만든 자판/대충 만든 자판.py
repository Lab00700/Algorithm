def solution(keymap, targets):
    answer = []
    min_key={}
    for key in keymap:
        for k in range(len(key)):
            if key[k] not in min_key:
                min_key[key[k]]=k+1
            elif min_key[key[k]]>k+1:
                min_key[key[k]]=k+1
    for key in targets:
        sum=0
        for k in key:
            if k not in min_key:
                sum=-1
                break
            sum+=min_key[k]
        answer.append(sum)
    return answer