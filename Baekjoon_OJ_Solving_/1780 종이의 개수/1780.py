def run(x,y,n):
    global a1 ,a2,a3
    board=arr[x][y]
    flag=1
    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j]!=board:
                run(x,y,n//3)
                run(x+n//3,y,n//3)
                run(x+(n//3)*2,y,n//3)

                run(x,y+n//3,n//3)
                run(x+n//3,y+n//3,n//3)
                run(x+(n//3)*2,y+n//3,n//3)
                
                run(x,y+(n//3)*2,n//3)
                run(x+n//3,y+(n//3)*2,n//3)
                run(x+(n//3)*2,y+(n//3)*2,n//3)
                return
    if board==-1:
        a1+=1
        return
    elif board==0:
        a2+=1
        return
    else:
        a3+=1
        return
    

n=int(input())
arr=[list(map(int,input().split()))for _ in range(n)]
a1=0
a2=0
a3=0
run(0,0,n)
print(a1)
print(a2)
print(a3)
