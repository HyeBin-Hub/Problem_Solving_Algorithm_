r,c=map(int,input().split())
sign=[(0,-1),(0,1),(-1,0),(1,0)] 
board=[list(input().rstrip()) for _ in range(r)]
res=[]
for row,i in enumerate(board):
    if "X" in i:
        for col in range(c):
            if i[col]=="X":
                total=0
                for j in sign:
                    a=row+j[0]
                    b=col+j[1]
                    if 0<=a<r and 0<=b<c and  board[a][b]==".": # 안에 바다가 있는 경우
                        total+=1
                    elif a<0 or a>=r :
                        total+=1
                    elif b<0 or b>=c: 
                        total+=1
                if 3<=total:
                    res.append((row,col))
for i,j in res:
    board[i][j]="."
cols=[]
for i in board:
    if "X" in i:
        for j in range(c):
            if i[j]=="X":
                cols.append(j)
            if i[c-j-1]=="X":
                cols.append(c-j-1)
for i in board:
    if "X" in i:
        print("".join(i[min(cols):max(cols)+1]))
