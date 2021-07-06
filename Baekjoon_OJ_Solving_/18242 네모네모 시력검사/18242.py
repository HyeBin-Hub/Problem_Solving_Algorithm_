import sys
input=sys.stdin.readline
n,m=map(int,input().split())
board=[list(input().rstrip()) for _ in range(n)]
start_row=0
start_col=0
end_row=0
end_col=0
length=0
for row in range(n):
    if "#" in board[row]:
        for col in range(m):
            if board[row][col]=="#":
                start_row=row
                start_col=col
                break
        for col in range(m-1,-1,-1):
            if board[row][col]=="#":
                end_row=row
                end_col=col
                break
        length=(end_col-start_col)+1
        break

if board[start_row][start_col+length//2]==".":
    print("UP")
    sys.exit()
elif board[start_row+length-1][start_col+length//2]==".":
    print("DOWN")
    sys.exit()
elif board[start_row+length//2][start_col]==".":
    print("LEFT")
    sys.exit()
elif board[start_row+length//2][end_col]==".":
    print("RIGHT")
    sys.exit()