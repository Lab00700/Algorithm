def solution(people, limit):
    people.sort()
    answer = 0
    l=len(people)
    i1=0
    i2=l-1
    while i2>=i1:
        answer+=1
        max_weight=people[i2]
        min_weight=people[i1]
        i2-=1
        if i2>=i1 and max_weight+min_weight<=limit:
            i1+=1
    return answer