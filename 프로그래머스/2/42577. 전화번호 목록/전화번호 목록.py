def solution(phone_book):
    max_len=0
    phone=set()
    phone_book=list(map(lambda x,y:[len(x),y],phone_book,phone_book)) #phone 길이와 number를 묶음
    phone_book.sort(key = lambda x:x[0]) #길이를 기준으로 정렬
    for l,ph in phone_book:
        temp=''
        t_len=0
        for p in ph: #한글자씩 불러오면서 중복된 접두사가 있는지 확인
            temp+=p
            t_len+=1
            if temp in phone: #중복된 접두사있으면 False
                return False
            if t_len>=max_len: #없다면, 접두사 최대 길이 갱신 후 추가
                phone.add(ph)
                max_len=l
                break
    return True