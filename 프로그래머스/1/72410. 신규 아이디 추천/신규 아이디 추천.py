def solution(new_id):
    l=['1','2','3','4','5','6','7','8','9','0','-','.','_']
    for i in range(26):
        l.append(chr(ord('a')+i))
    answer = ''
    new_id=new_id.lower()
    dot=False
    for n in new_id:
        if n in l:
            if n=='.' and len(answer)!=0:
                dot=True
            elif n!='.':
                if dot:
                    answer+='.'
                    dot=False
                answer+=n
    if len(answer)==0:
        answer='a'
    print(answer)
    if len(answer)>15:
        if answer[14]=='.':
            answer=answer[:14]
        else:
            answer=answer[:15]
    while len(answer)<3:
        answer+=answer[-1]
    return answer