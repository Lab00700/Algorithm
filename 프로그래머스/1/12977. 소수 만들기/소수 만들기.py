def solution(nums):
    answer = 0
    temp=[]
    for i in range(max(nums)*3):
        temp.append(0)
    for i in range(len(temp)):
        for k in range(i,len(temp),i+1):
            temp[k]+=1
    for i in range(len(nums)):
        for k in range(i+1,len(nums)):
            for t in range(k+1,len(nums)):
                sum=nums[i]+nums[k]+nums[t]
                if temp[sum-1]<=2:
                    answer+=1
                    
    return answer