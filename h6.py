nums = [*map(int, input().split())]
l = 0
r = len(nums) - 1
a = []
for i in range(len(nums)):
    a.append(nums[i] * nums[i])
c = r
while (l <= r):
    if (a[l] >= a[r]):
        nums[c] = a[l]
        l += 1
    else:
        nums[c] = a[r]
        r -= 1

    c -= 1
print(nums)