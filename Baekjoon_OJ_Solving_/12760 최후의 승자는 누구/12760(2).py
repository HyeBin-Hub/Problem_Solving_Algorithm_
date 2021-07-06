n,m=map(int,input().split())
arr=[list(map(int,input().split()))for _ in range(n)]
cnt={}


for i in range(m):
    dic={}
    for ind,j in enumerate(range(n),1):
        dic[ind]=arr[j][i]

    a=max(dic.values())
    for k,v in dic.items():
        if v==a:
            if k in cnt:
                cnt[k]+=1
            else:
                cnt[k]=1

res=[]
for k,v in cnt.items():
    if max(cnt.values())==v:
        res.append(k)
print(*sorted(res))