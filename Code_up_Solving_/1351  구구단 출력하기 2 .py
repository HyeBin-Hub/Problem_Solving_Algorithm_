n,m=map(int,input().split())
for i in range(n,m+1):
    for j in range(1,10):
        print("{}*{}={}".format(i,j,i*j))
