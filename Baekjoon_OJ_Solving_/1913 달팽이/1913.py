n=int(input())
a=int(input())
board=[[0]*n for _ in range(n)]

# 가운데 먼저 찾기
row,col=n//2,n//2 # 처음 시점 (1찾음)
number=1
step=1

board[row][col]=number

for _ in range(n//2):
    # 위로 이동
    for _ in range(step):
        row-=1
        number+=1
        board[row][col]=number
    # 오른쪽으로 이동
    for _ in range(step):
        col+=1
        number+=1
        board[row][col]=number

    step+=1

    # 아래로 이동
    for _ in range(step):
        row+=1
        number+=1
        board[row][col]=number
    # 왼쪽으로 이동
    for _ in range(step):
        col-=1
        number+=1
        board[row][col]=number

    step+=1

# 위로 이동 (위로는 3번 밖에 안가자나)
for _ in range(step-1):
    row-=1
    number+=1
    board[row][col]=number

for i in board:
    print(*i)

flag=0
for ind,i in enumerate(board):
    for ind2,j in enumerate(i):
        if j==a:
            print(ind+1,ind2+1)
            flag=1
            break
    if flag:
        break
