from collections import deque
import sys
input=sys.stdin.readline
n = int(input())
arr = deque(map(int, input().split()))
stack = []
i = 1
while arr:
    if arr and arr[0] == i:
        arr.popleft()
        i += 1
    else:
        stack.append(arr.popleft())
    while stack and stack[-1] == i:
        stack.pop()
        i += 1
        
print("Nice" if not stack else "Sad")