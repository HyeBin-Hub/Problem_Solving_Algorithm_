n=int(input())
for i in range(n):
    ys,ks=0,0
    for j in range(9):
        y,k=map(int,input().split())
        ys+=y
        ks+=k
    if ys>ks:
        print("Yonsei")
    elif ys<ks:
        print("Korea")
    else:
        print("Draw")