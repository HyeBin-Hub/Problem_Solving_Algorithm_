

t = int(input())

for _ in range(t):
    n = int(input())
    left=1
    right=n
    res=[]
    while left<=right:
        mid=(left+right)//2
        if (mid*(mid+1))//2<=n:
            res.append(mid)
            left=mid+1
        else:
            right=mid-1
    print(res[-1])
            
            
