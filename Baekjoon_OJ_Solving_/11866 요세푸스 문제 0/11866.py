from collections import deque
n,m=map(int,input().split())
deq=deque(range(1,n+1))
print("<",end="")
while len(deq)!=1:
    deq.rotate(-(m-1))
    print(deq.popleft(),end=", ")
print(str(deq[0])+">")

