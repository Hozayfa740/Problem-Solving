from collections import defaultdict
s1 = input()
s2 = input()
result = []
g = defaultdict(int)
check = defaultdict(int)
for ch in s2:
    g[ch] += 1
for ch in s1[:len(s2) - 1]:
    check[ch] += 1

c = 0
for r in range(len(s2) - 1, len(s1)):
    check[s1[r]] += 1
    if all(g[ch] == check[ch] for ch in g):
          result.append(c)
    check[s1[c]] -= 1
    c += 1

print(result)







