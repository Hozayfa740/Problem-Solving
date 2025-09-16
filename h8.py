n, k = map(int, input().split())
a = list(map(int, input().split()))
arr = [(a[i], i + 1) for i in range(len(a))]
arr.sort()
check=1
l, r = 0, n - 1
while l < r:
    s = arr[l][0] + arr[r][0]
    if s == k:
        print(arr[l][1], arr[r][1])
        check=0
        break
    elif s < k:
        l += 1
    else:
        r -= 1
if check:
    print("IMPOSSIBLE")
