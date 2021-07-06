import sys
def run(row,col):
    if row>=n or col >=n:
        return
    if (row,col)==(n-1,n-1):
        print("HaruHaru")
        sys.exit()

    move=board[row][col]

    if move==0:
        return

    # 오른쪽으로 이동
    run(row,col+move)
    # 아래로 이동
    run(row+move,col)

n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
run(0,0)
print("Hing")