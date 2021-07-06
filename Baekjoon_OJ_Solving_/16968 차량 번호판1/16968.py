s=input().rstrip()
res=1
pre=""
total=1
for i in s:
    if i=="c":
        res=26
    if i=="d":
        res=10
    if i==pre:
        res-=1
    total*=res
    pre=i
print(total)