n,t=map(int,input().split())
x=0
y=0
d=2
time=0

for _ in range(n):
    ti,si=input().rstrip().split()
    ti=int(ti)

    move=ti-time

    if d==0: # 왼쪽
        x-=move
    elif d==1 : # 위
        y+=move
    elif d==2:  # 오른쪽
        x+=move
    else:
        y-=move

    if si=="right":
        d=(d+1)%4
    else:
        d=(d-1)%4

    time=ti

move=t-time

if d==0: # 왼쪽
    x-=move
elif d==1 : # 위
    y+=move
elif d==2:  # 오른쪽
    x+=move
else:
    y-=move


print(x,y)



