from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[list(input().rstrip()) for _ in range(n)]

board=[]
board2=deque([])
for i in range(n):
    board.append(arr[i]+arr[i][::-1])
    board2.appendleft(arr[i]+arr[i][::-1])

board2=list(board2)
res=board+board2

err_n,err_m=map(int,input().split())
if res[err_n-1][err_m-1]=="#":
    res[err_n-1][err_m-1]="."
else:
    res[err_n-1][err_m-1]="#"
for i in res:
    print("".join(i))