n,m=map(int,input().split())
board=[list(input())for _ in range(n)]
res=[]
for i in range(n-7):
    for j in range(m-7):
        res_w=0
        res_b=0
        for row in range(i,i+8):
            for col in range(j,j+8):
                if (row+col)%2==0:
                    if board[row][col]!="W":
                        res_w+=1
                    if board[row][col]!="B":
                        res_b+=1
                else:
                    if board[row][col]!="B":
                        res_w+=1
                    if board[row][col]!="W":
                        res_b+=1
        res.append(res_b)
        res.append(res_w)
print(min(res))