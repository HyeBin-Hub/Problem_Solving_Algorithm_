n=int(input())
for i in range(n):
    h,w,n=map(int,input().split())
    if n%h!=0:
        print((n%h)*100+(n//h+1))
    else:
        print(h*100+(n//h))