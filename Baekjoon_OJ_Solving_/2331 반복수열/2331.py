a,p=input().rstrip().split()

p=int(p)
res=[int(a)]

while 1:
    total=0
    for i in a:
        total+=int(i)**p
    if total not in res:
        res.append(total)
    elif total in res:
        a=res.index(total)
        print(len(res)-len(res[a:]))
        break
    a=list(str(total))
   




