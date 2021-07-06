import sys
from collections import deque
n=int(input())
input=sys.stdin.readline
deq=deque()
for i in range(n):
    s=input().split()
    if s[0]=="push_front":
        deq.appendleft(s[1])
    elif s[0]=="push_back":
        deq.append(s[1])
    elif s[0]=="pop_front":
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif s[0]=="pop_back":
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif s[0]=="size":
        print(len(deq))
    elif s[0]=="empty":
        if deq:
            print(0)
        else:
            print(1)
    elif s[0]=="front":
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif s[0]=="back":
        if deq:
            print(deq[-1])
        else:
            print(-1)