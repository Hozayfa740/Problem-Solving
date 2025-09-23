nums=[*map(int,input().split())]
l=0
r=1
for i in range(len(nums)-1):
    if(nums[l]==0 and nums[r]!=0):
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
        r+=1
    elif (nums[l] == 0 and nums[r] == 0):
        nums[l], nums[r] = nums[r], nums[l]
        r += 1
    else:
        l+=1
        r+=1
print(*nums)

