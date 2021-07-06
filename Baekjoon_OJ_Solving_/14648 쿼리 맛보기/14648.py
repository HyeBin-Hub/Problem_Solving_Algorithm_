import sys
input=sys.stdin.readline
n,q=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(q):
    a=list(map(int,input().split()))
    if a[0]==1 :
        print(sum(arr[a[1]-1:a[2]]))
        arr[a[1]-1],arr[a[2]-1]=arr[a[2]-1],arr[a[1]-1]
    elif a[0]==2:
        print(sum(arr[a[1]-1:a[2]])-sum(arr[a[3]-1:a[4]]))