import sys
input=sys.stdin.readline
n,m=map(int,input().split())
res=[0]*(n+1)
arr=[list(map(int,input().split()))for _ in range(n)]
for i in range(m):
    a=[]
    for j in range(n):
        a.append(arr[j][i])
    max_a=max(a)
    for ind,j in enumerate(range(n),1):
        if max_a==arr[j][i]:
            res[ind] +=1
maxs=0
for ind,i in enumerate(res[1:],1):
    if max(res)==i:
        print(ind,end=" ")