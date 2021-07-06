
n=int(input())
board=[list(input().rstrip()) for _ in range(n)]
board2=[list(input().rstrip()) for _ in range(n)]

a=[(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,1),(1,-1)]

opened=0
for row in range(n):
    for col in range(n):
        if board2[row][col]=="x" and board[row][col]=="*":
            opened=1
            break
    if opened:
        break
    
for row,x in enumerate(board2):
    for col,i in enumerate(x):
        if opened and board[row][col]=="*":
            board2[row][col]="*"
            continue
        if i=="x":
            count=0
            for j in a:
                if 0<=row+j[0]<n and 0<=col+j[1]<n:
                    if board[row+j[0]][col+j[1]]=="*":
                        count+=1   
            board2[row][col]=count
 

for i in board2:
    print("".join(map(str,i)))         
            

