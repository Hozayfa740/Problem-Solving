from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))
p = defaultdict(int)
ans = 0
c = 0
for r in range(n):
    p[a[r]] += 1
    while len(p) > k:
        p[a[c]] -= 1
        if p[a[c]] == 0:
            p.pop(a[c])
        c += 1
    ans += (r - c + 1)
print(ans)

