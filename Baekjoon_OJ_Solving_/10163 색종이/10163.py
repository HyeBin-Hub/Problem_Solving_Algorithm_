arr=[[0]*101 for _ in range(101)]
n=int(input())
for i in range(1,n+1):
    x,y,w,h=map(int,input().split())
    for col in range(x,x+w):
        for row in range(y,y+h):
            arr[col][row]=i
cnt=[0]*(n+1)
for row in range(101):
    for col in range(101):
        cnt[arr[row][col]]+=1
for i in cnt[1:]:
    print(i)
