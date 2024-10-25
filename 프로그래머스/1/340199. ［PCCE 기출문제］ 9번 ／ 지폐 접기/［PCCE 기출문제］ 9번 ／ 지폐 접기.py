def solution(wallet, bill):
    answer = 0
    wallet.sort()
    while wallet[0]<bill[0] or wallet[1]<bill[1]:
        bill[bill.index(max(bill))]=int(max(bill)/2)
        bill.sort()
        answer+=1
    return answer