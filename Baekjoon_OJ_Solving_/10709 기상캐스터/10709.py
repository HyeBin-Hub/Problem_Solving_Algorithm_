h,w=map(int,input().split())
board=[[0]*w for _ in range(h)]
count=0
for row in range(h):
    arr=list(input().rstrip())
    if arr[0]==".":
        board[row][0]=-1
    for col in range(1,w):
        if arr[col]==".":
            if board[row][col-1]==0:
                board[row][col]=1
            elif board[row][col-1]==-1:
                board[row][col]=-1
            elif board[row][col-1]>=1:
                count+=1
                board[row][col]=board[row][col-1]+1
print("\n".join(" ".join(map(str,i))for i in board))






