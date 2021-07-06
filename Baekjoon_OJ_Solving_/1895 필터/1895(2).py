def filters(start_row,start_col):
    global count
    arr=[]
    for col in range(start_col,start_col+3):
        for row in range(start_row,start_row+3):
            arr.append(board[row][col])
    arr.sort()
    if arr[4]>=t:
        count+=1
    
r,c=map(int,input().split())
board=[list(map(int,input().split()))for i in range(r)]
t=int(input())
count=0
for row in range(r-2):
    for col in range(c-2):
        filters(row,col)
print(count)
