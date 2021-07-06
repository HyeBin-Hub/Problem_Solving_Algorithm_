
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
def run(n):
    res=[]
    for i in range(2,n+1):
        for j in range(i,n+1,i):
            if j not in res:
                res.append(j)
    return res
print(run(n)[k-1])

