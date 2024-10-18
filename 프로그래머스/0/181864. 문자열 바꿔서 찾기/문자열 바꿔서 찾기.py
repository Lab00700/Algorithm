def solution(myString, pat):
    myString=myString.replace("A","C")
    myString=myString.replace("B","A")
    myString=myString.replace("C","B")
    answer = 1 if pat in myString else 0
    return answer