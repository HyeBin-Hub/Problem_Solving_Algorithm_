import sys
n=int(input())
x=0
y=0
step=1
total=0
while 1:
    # 위 (7에서 9일때까지는 여기서 해결)
    a=total+step
    if n==total+step:
        print(x,y+step)
        sys.exit()
    elif total<n<total+step:
        print(x,y+(n-total))
        sys.exit()
    y+=step
    total+=step
    
    # 오른쪽
    a=total+step
    if n==total+step:
        print(x+step,y)
        sys.exit()
    elif total<n<total+step:
        print(x+(n-total),y)
        sys.exit()
    x+=step
    total+=step
    
    step+=1
    
    # 아래
    a=total+step
    if n==total+step:
        print(x,y-step)
        sys.exit()
    elif total<n<total+step:
        print(x,y-(n-total))
        sys.exit()
    y-=step
    total+=step

    # 왼쪽
    a=total+step
    if n==total+step:
        print(x-step,y)
        sys.exit()
    elif total<n<total+step:
        print(x-(n-total),y)
        sys.exit()
    x-=step
    total+=step

    step+=1