n,l=map(int,input().split())
hi=list(map(int,input().split()))
hi.sort()
for i in hi:
    if l>=i:
        l+=1
print(l)

