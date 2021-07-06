from collections import deque
import sys
input=sys.stdin.readline
left=deque(list(input().rstrip()))
right=deque()
for i in range(int(input())):
    command=input().rstrip()
    if command.split()[0]=="P":
        left.append(command.split()[1])
    elif command=="L":
        if not left:
            continue
        right.appendleft(left.pop())
    elif command=="B":
        if not left :
            continue
        left.pop()
    elif command=="D":
        if not right:
            continue
        left.append(right.popleft())
print("".join(left+right))
