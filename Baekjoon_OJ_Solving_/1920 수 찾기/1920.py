def run(a,search,start,end):
    if start > end:
        return 0
    mid=(start+end)//2
    if a[mid]==search:
        return 1
    elif a[mid]>search:
        return run(a,search,start,mid-1)
    else:
        return run(a,search,mid+1,end)

import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
a.sort()
m=int(input())
b=list(map(int,input().split()))
for i in b:
    print(run(a,i,0,n-1))