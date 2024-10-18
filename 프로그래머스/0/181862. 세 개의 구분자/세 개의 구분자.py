def solution(myStr):
    myStr=myStr.replace('a', ' ')
    myStr=myStr.replace('b', ' ')
    myStr=myStr.replace('c', ' ')
    myStr=myStr.split(' ')
    for i in range(myStr.count("")):
        myStr.remove("")
    if len(myStr)==0:
        myStr.append("EMPTY")
    return myStr