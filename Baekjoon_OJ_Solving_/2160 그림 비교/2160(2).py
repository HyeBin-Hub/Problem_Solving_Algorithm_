from itertools import combinations
import sys
input=sys.stdin.readline
n=int(input())
board=[input().rstrip() for _ in range(n*5)]
res=list(combinations(range(n),2))

arr=[board[row:row+5] for row in range(0,n*5,5)]

mins=[]

for i in res:

    total=0
    for k,r in zip(arr[i[0]],arr[i[1]]):
        for q,p in zip(k,r):
            if q!=p:
                total+=1
    mins.append(total)
print(res[mins.index(min(mins))][0]+1,res[mins.index(min(mins))][1]+1)



