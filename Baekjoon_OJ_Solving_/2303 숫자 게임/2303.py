from itertools import combinations
import sys
input=sys.stdin.readline
n=int(input())
max_value={}
for j in range(n):
    arr=list(map(int,input().split()))
    res=list(combinations(arr,3))
    maxs=[]
    for i in res:
        maxs.append(list(str(sum(i)))[-1])
    max_value[j]=int(max(maxs))
res=sorted(max_value.items(),key=lambda x:(-x[1],-x[0]))
print(res[0][0]+1)