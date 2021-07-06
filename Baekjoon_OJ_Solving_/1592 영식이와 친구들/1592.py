import sys
n,m,l=map(int,input().split())

cnt=[0]*(n+1)
cnt[1]=1

loc=1

while 1:
    if cnt[loc]%2==0: 
        loc=loc-l
        if loc<1:
            loc+=n
        cnt[loc]+=1

    else: 
        loc=loc+l
        if loc>n:
            loc-=n
        cnt[loc]+=1
    
    for j in cnt:
        if j>=m:
            print(sum(cnt)-1)
            sys.exit()
        



