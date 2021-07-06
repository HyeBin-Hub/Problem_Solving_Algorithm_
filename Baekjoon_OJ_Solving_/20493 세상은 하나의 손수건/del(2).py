n,t=map(int,input().split())
mv=[(-1,0),(0,1),(1,0),(0,-1)] # 왼쪽 위 오른쪽 아래
d=2
x=0
y=0
time=0
for _ in range(n):
    ti,si=input().rstrip().split()
    ti=int(ti)

    temp=ti-time

    mv_x,mv_y=mv[d]

    x+=mv_x*temp
    y+=mv_y*temp

    if si=="right":
        d=(d+1)%4
    else:
        d=(d-1)%4

    time=ti

temp=t-time

mv_x,mv_y=mv[d]

x+=mv_x*temp
y+=mv_y*temp

print(x,y)