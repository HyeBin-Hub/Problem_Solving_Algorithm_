from collections import Counter
import sys
input = sys.stdin.readline

n,m=map(int,input().split())

arr=[input().rstrip() for _ in range(n)]

s=""
for col in range(m):
    t=[]
    for row in range(n):
        t.append(arr[row][col])
    a=sorted(Counter(t).items(),key=lambda x:(-x[1],x[0]))
    s+=a[0][0]

total=0
for i in arr:
    cnt=0
    for ind,j in enumerate(i):
        if j!=s[ind]:
            cnt+=1   
    total+=cnt
print(s)
print(total)