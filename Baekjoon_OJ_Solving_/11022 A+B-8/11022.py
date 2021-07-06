import sys
input=sys.stdin.readline
n=int(input())
i=0
while n!=0:
    a,b=map(int,input().split())
    i+=1
    print("Case #{}: {} + {} = {}".format(i,a,b,a+b))
    n-=1