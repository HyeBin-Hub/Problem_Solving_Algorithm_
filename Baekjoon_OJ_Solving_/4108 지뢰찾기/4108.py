def run(row,col):
    count=0

    # 좌 (0,4)일때는 왼쪽만 확인
    if col !=0 :
        if board[row][col-1]=="*" :
            count+=1

    # 우 (0,0)일때는 오른쪽만 확인
    if col != c-1:
        if board[row][col+1]=="*":
            count+=1

    # 상 (0,0)일때는 밑에만 확인하면됨
    if row!=0:
        if board[row-1][col]=="*":
            count+=1
    # 하 (4,0)일때는 위에만 확인하면됨
    if row!=r-1:
        if board[row+1][col]=="*":
            count+=1
    
    # 오른쪽 위
    if row!=0 and col!=c-1:
        # 위
        if board[row-1][col+1]=="*":
            count+=1
    # 왼쪽 아래
    if row!=r-1 and col!=0:
        if board[row+1][col-1]=="*":
            count+=1

    # 오른쪽 아래
    if row!=r-1 and col!=c-1:
        if board[row+1][col+1]=="*":
            count+=1
    # 왼쪽 위
    if row!=0 and col !=0:
        if board[row-1][col-1]=="*":
            count+=1

    return count

while  1 :
    r,c=map(int,input().split())
    if r==0 and c==0:
        break
    board=[list(map(str,(input().rstrip()))) for _ in range(r)]
    for row in range(r):
        for col in range(c):
            if board[row][col]==".":
                count_num=run(row,col)
                board[row][col]=count_num
    for i in board:
        print("".join(map(str,i)))
    


