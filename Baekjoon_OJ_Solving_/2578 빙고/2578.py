import sys
def run():
    count=0
 
    # 가로 확인
    for i in range(5):
        if board[i]==[1,1,1,1,1]:
            count+=1

    # 세로 확인
    
    for col in range(5):
        total=0
        for row in range(5):
            if board[row][col]==1:
                total+=1
        if total==5:
            count+=1

    # 왼쪽 대각선확인
    total=0
    for i in range(5):
        if board[i][i]==1:
            total+=1
    if total==5:
        count+=1
    # 오른쪽 대각선 확인
    total=0
    for i in range(5):
        if board[i][5-i-1]==1:
            total+=1
    if total==5:
        count+=1

    if count>=3:
        return 1
    else:
        return 0
   

me=[list(map(int,input().split()))for _ in range(5)]
t=[list(map(int,input().split()))for _ in range(5)]
board=[[0]*5 for _ in range(5)]


for x,i in enumerate(t):
    for y,j in enumerate(i):
        for row in range(5):
            if j in me[row]:
                for col in range(5):
                    if me[row][col]==j:
                        board[row][col]=1
                        break
                if run()==1:
                    print(x*5+y+1)
                    sys.exit()
                
                        
