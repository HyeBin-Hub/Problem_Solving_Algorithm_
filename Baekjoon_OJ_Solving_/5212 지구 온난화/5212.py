import copy
r,c=map(int,input().split())
sign=[(0,-1),(0,1),(-1,0),(1,0)] 
board=[list(input().rstrip()) for _ in range(r)]
result=copy.deepcopy(board)
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
                    result[row][col]="."

start_y, end_y = 0, 0
for i in range(r):
    if 'X' in result[i]:
        start_y = i
        break
for i in range(r-1, -1,-1):
    if 'X' in result[i]:       
        end_y = i
        break

tmp = []
for j in range(c):
    for i in range(start_y, end_y + 1):
        if 'X' == result[i][j]:
            tmp.append(j)
            break

for y in range(start_y, end_y+1):
    print("".join(result[y][tmp[0]:tmp[-1]+1]))