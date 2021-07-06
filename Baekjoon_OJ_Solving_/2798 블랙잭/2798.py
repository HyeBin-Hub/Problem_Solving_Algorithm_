from itertools import combinations
n,m=map(int,input().split())
arr=list(map(int,input().split()))
res=list(combinations(arr,3))
result=0
for i in res:
    if sum(i)<=m:
        result=max(result,sum(i))
print(result)
