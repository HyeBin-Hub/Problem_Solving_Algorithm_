import sys
input = sys.stdin.readline

n,m=map(int,input().split())

arr=[input().rstrip() for _ in range(n)]

s=""
for col in range(m):
    d=dict()
    d["A"],d["T"],d["G"],d["C"]=0,0,0,0
    for row in range(n):
        d[arr[row][col]]+=1
    d=sorted(d.items(),key=lambda x:(-x[1],x[0]))
    s+=d[0][0]

total=0
for i in arr:
    cnt=0
    for ind,j in enumerate(i):
        if j!=s[ind]:
            cnt+=1   
    total+=cnt
print(s)
print(total)