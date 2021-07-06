from itertools import combinations
import sys
input=sys.stdin.readline
n=int(input())
S=[]
B=[]
for i in range(n):
    s,b=map(int,input().split())
    S.append(s)
    B.append(b)
q=sys.maxsize
for i in range(1,n+1):
    a=list(combinations(S,i))
    b=list(combinations(B,i))
    for r,t in zip(a,b):
        res=1
        for j in r:
            res*=j
        q=min(q,abs(res-sum(t)))
print(q)

 