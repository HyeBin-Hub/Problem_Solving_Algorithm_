import sys
input=sys.stdin.readline
def run():
    n,m=map(int,input().split())
    arr=list(range(1,n+1))
    num=0
    print("<",end="")
    while len(arr)!=1:
        num=(num+m-1)%len(arr)
        print(arr.pop(num),end=", ")
    print(str(arr[0])+">")
run()