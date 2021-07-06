import sys
input=sys.stdin.readline
from itertools import combinations
n,m=map(int,input().split())
arr=list(range(1,n+1))
res=list(combinations(arr,m))
print("\n".join(" ".join(map(str,i)) for i in res))














