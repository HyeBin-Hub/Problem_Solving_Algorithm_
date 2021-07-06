a=list(map(int,input().split()))
z=False
for i in a:
    if i >170:
        z=True
    else:
        z=False
        q=i
        break
if z==True:
    print("PASS")
else:
    print("CRASH",q)
