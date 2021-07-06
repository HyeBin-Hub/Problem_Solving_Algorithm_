from itertools import combinations
import sys
input=sys.stdin.readline
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
res=list(combinations(list(range(1,n+1)),n//2))

a_min=sys.maxsize

for i in range(len(res)//2):
    total1=0
    for j in res[i]:
        for k in res[i]:
            total1+=board[j-1][k-1]

    total2=0
    for j in res[-i-1]:
        for k in res[-i-1]:
            total2+=board[j-1][k-1]

    total=abs(total1-total2)
    a_min=min(a_min,total)
print(a_min)