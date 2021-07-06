import sys
input=sys.stdin.readline
board=list(input().rstrip().split("."))
flag = True
for i in range(len(board)):
    if len(board[i])%2!=0:
        flag = False
        break
    x_rem=0
    res=[]  
    while len(board[i])!=x_rem:
        if len(board[i])-x_rem >=4: # AAAA
            res.append("AAAA")
            x_rem+=4
        elif len(board[i])-x_rem >=2:
            res.append("BB")
            x_rem+=2
    board[i]="".join(res)

# print(board)

if flag:
    print('.'.join(board))
else:
    print(-1) 
