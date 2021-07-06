import sys
input=sys.stdin.readline
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    res=[]
    for j in range(n):
        k,*d,momey=map(int,input().split())
        res.append((k,[*d],momey))
    arr=list(map(int,input().split()))
    total=0
    for j in res:
        a=sys.maxsize
        for k in j[1]:
            a=min(a,arr[k-1])
        total+=a*j[-1]
    print(total)