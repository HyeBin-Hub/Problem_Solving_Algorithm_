
h,w=map(int,input().split())

n=int(input())

a=[[0 for i in range(h)]for j in range(w)]  

for i in range(n):
    i,d,x,y=map(int,input().split())
    for j in range(i):
        if d==0:
            a[x-1][y-1+j]=1
        elif d==1:
            a[x-1+j][y-1]=1
for i in range(h):
    for j in range(w):
        print(a[i][j],end="")
    print(end="\n")













































