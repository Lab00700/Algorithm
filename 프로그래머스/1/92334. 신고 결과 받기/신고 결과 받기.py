def solution(id_list, report, k):
    dic={}
    rep={}
    mail={}
    answer = []
    for i in id_list:
        mail[i]=0
    for r in report:
        if r not in dic:
            dic[r]=1
            if r.split()[1] not in rep:
                rep[r.split()[1]]=1
            else:
                rep[r.split()[1]]+=1
    for d in dic.keys():
        a,b=d.split()
        if rep[b]>=k:
            mail[a]+=1
    for m in mail.keys():
        answer.append(mail[m])
    return answer