"""
from collections import deque
n=int(input())
s=list(map(int,input().split()))
deq=deque(s)
deq.rotate(1)

for i in range(n):
    deq.rotate(-1)
    for j in deq:
        print(j,end=" ")
    print()
"""



"""
from collections import deque
n=int(input())
s=list(map(int,input().split()))
s=deque(s)
s.rotate(1)
for i in range(n):
    s.rotate(-1)
    for j in s:
        print(j,end=" ")
    print()
"""

from collections import deque
n=int(input())
s=list(map(int,input().split()))
s=deque(s)
s.rotate(1)
for i in range(n):
    s.rotate(-1)
    for j in s:
        print(j,end=" ")
    print()
    


































































