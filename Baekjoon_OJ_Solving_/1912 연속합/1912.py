import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
res=[-1001]
for i in arr:
    res.append(max(res[-1]+i,i))
print(max(res))