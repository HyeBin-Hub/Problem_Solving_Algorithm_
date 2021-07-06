import sys
def run(size,row,col):
    global num
    if size==2:
        if row==r and col==c : # 1사분면
            print(num)
            return
        num+=1
        if row==r and col+1==c: # 2사분면
            print(num)
            return
        num+=1
        if row+1==r and col==c: # 3사분면
            print(num)
            return
        num+=1
        if row+1==r and col+1==c: # 4사분면
            print(num)
            return
        num+=1

    else:
        run(size//2,row,col) # 1사분면
        run(size//2,row,col+size//2) # 2사분면
        run(size//2,row+size//2,col)
        run(size//2,row+size//2,col+size//2)

n,r,c=map(int,input().split())
num=0
run(2**n*n**2,0,0)