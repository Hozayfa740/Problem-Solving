
n, k = map(int, input().split())
a = list(map(int, input().split()))
s=0
c=0
count=0
for i in range(n):
    s += a[i]
    while(s>k):
        s-=a[c]
        c+=1
        if s<0:
            s=0
    if s==k:
        count+=1
print(count) 