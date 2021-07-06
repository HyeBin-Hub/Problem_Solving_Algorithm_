
n,t=map(int,input().split())
x=y=0
direction=1 # 0: 위쪽 1: 오른쪽 2: 아래쪽 3: 왼쪽
time=0

for _ in range(n):
    ti,si=input().rstrip().split()

    ti=int(ti)

    # 이동하기
    movement=ti-time

    if direction==0:
        y+=movement
    elif direction==1:
        x+=movement
    elif direction==2:
        y-=movement
    else:
        x-=movement

    # 방향 전환
    if si=="right":
        direction=(direction+1)%4
    else:
        direction=(direction-1)%4

    time=ti

movement=t-time

if direction==0:
    y+=movement
elif direction==1:
    x+=movement
elif direction==2:
    y-=movement
else:
    x-=movement
    
print(x,y)

































    



    
