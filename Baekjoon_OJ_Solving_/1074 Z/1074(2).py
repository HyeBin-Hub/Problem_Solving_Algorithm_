import sys
def run(size,start_row,start_col,num):
    end_row=start_row+size
    end_col=start_col+size

    if start_row<=r<end_row and start_col <=c<end_col:
        if size==1:
            print(num)
            sys.exit()
        
        next_size=size//2
        run(next_size,start_row,start_col,num)
        run(next_size,start_row,start_col+next_size,num+next_size**2)
        run(next_size,start_row+next_size,start_col,num+next_size**2*2)
        run(next_size,start_row+next_size,start_col+next_size,num+next_size**2*3)
n,r,c=map(int,input().split())
run(2**n,0,0,0)