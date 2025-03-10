def solution(elements):
    val=set()
    length=len(elements)
    
    i=0
    while i<length:
        sum=elements[i]
        val.add(elements[i])
        k=(i+1)%length
        while k!=i:
            sum+=elements[k]
            val.add(sum)
            k+=1
            if k==length:
                k=0
        i+=1

    return len(val)