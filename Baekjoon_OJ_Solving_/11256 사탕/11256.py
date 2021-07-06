t=int(input())
for _ in range(t):
    j,n=map(int,input().split())
    res=[]
    for _ in range(n):
        ri,ci,=map(int,input().split())
        res.append(ri*ci)

    res.sort(reverse=True)

    count=0
    for i in res:
        j-=i
        if j>0:
            count+=1
    print(count+1)

