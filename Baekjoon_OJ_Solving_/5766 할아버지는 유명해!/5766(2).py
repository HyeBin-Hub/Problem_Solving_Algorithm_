

while 1:
    n,m=map(int,input().split())
    if n==0:
        break
    board=[list(map(int,input().split()))for _ in range(n)]
    cnt={}
    for i in board:
        for j in i:
            if j in cnt:
                cnt[j]+=1
            else:
                cnt[j]=1
    a=sorted(cnt.items(),key=lambda x:x[1],reverse=True)
    val=list(set(cnt.values()))
    result=list(map(lambda x: x[0] if x[1]==val[-2] else 0 , a))
    print(" ".join(map(str,[i for i in sorted(result) if i!=0 ])))

