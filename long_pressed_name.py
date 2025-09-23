name=input()
typed=input()
pre=name[0]
c=0
f=1
if(len(name)>len(typed)):
    f=0
else:
    for i in typed:
        if i==name[c] and c<=len(name):
            pre=name[c]
            c+=1
        elif i==pre:
            continue
        else:
            f=0
            break
print("true"if f!=0 else"false")