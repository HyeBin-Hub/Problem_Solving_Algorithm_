from collections import deque
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
deq=deque(list(range(1,n+1)))
res=[]
while len(deq)!=0:
    deq.rotate(-k)
    res.append(deq.pop())
print("<"+", ".join(map(str,res))+">")

