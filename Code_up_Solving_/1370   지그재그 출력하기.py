h,r=map(int,input().split())

def replay(h,r):
    for i in range(h):
        for j in range(i):
            print(" ",end="")
        for j in range(1):
            print("*",end="")
        print()
    for i in range(h-2,-1,-1):
        for j in range(i):
            print(" ",end="")
        for j in range(1):
            print("*",end="")
        print()


for i in range(r):
    replay(h,r)
    

