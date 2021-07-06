import sys
input=sys.stdin.readline
def run():
    n=int(input())
    total=0

    board=[[0]*500 for _ in range(500)]

    for _ in range(n):
        x1,y1,x2,y2=map(int,input().split())
        for i in range(x1,x2):
            for j in range(y1,y2):
                board[i][j]=1

    for i in board:
        if 1 in i:
            total+=sum(i)
    print(total)
run()
    