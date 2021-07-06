n,m=map(int,input().split())
board=[[0]*100 for _ in range(101)]

for i in range(n):
    lx,ly,rx,ry=map(int,input().split())
    for row in range(lx-1,rx):
        for col in range(ly-1,ry):
            board[row][col]+=1
cnt=0
for i in board:
    for j in i:
        if j>m:
            cnt+=1
print(cnt)
