import sys
from collections import defaultdict
n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

p = defaultdict(int)
p[0] = 1
pxsum = 0
count = 0

for i in range(n):
    pxsum += a[i]
    count += p[pxsum - k]
    p[pxsum] += 1

print(count)


