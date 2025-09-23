from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

p = defaultdict(int)
have = 0
need = k
ans = n + 1
left = 0
for right in range(n):
    if 1 <= a[right] <= k:
        if p[a[right]] == 0:
            have += 1
        p[a[right]] += 1

    while have == need:
        ans = min(ans, right - left + 1)
        if 1 <= a[left] <= k:
            p[a[left]] -= 1
            if p[a[left]] == 0:
                have -= 1
        left += 1
print(0 if ans == n + 1 else ans)
