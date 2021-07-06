from collections import deque
import sys 
input=sys.stdin.readline
n,m=map(int,input().split())
arr=list(map(int,input().split()))
deq=list(range(1,n+1))
count=0
for i in arr:
    deq=deque(deq)
    if deq.index(i)>len(deq)//2:
        a=deq.index(i)
        deq.rotate(len(deq)-a)
        deq.popleft()
        count+=len(deq)+1-a
    else:
        a=deq.index(i)
        deq.rotate(-len(deq)-a)
        deq.popleft()
        count+=a
print(count)