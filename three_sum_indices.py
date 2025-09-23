n, k = map(int, input().split())
a = list(map(int, input().split()))
arr = [(a[i], i + 1) for i in range(n)]
arr.sort()
for i in range(n):
    l, r = 0, n - 1
    target = k - arr[i][0]
    while l < r:
        if l == i:
            l += 1
            continue
        if r == i:
            r -= 1
            continue
        s = arr[l][0] + arr[r][0]
        if s == target:
            print(arr[i][1], arr[l][1], arr[r][1])
            exit()
        elif s < target:
            l += 1
        else:
            r -= 1
print("IMPOSSIBLE")
