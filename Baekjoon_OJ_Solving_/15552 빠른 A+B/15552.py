import sys
input=sys.stdin.readline
n=int(input().rstrip())
while n!=0:
    n-=1
    a,b=map(int,input().split())
    print(a+b)