import sys
input=sys.stdin.readline
l=int(input())
arr=list(map(int,input().split()))
n=int(input())
arr.sort()
if n in arr :
    print(0)
    sys.exit()

if len(arr)==1:
    print(arr[0]-1-n)
    sys.exit()

for i in range(l-1):
    if arr[i]< n <arr[i+1]:
        res_f=list(range(arr[i]+1,n))
        res_b=list(range(n,arr[i+1]))
        print(len(res_b)*len(res_f)+len(res_b)-1)
    else:
        if min(arr)>n:
            res_f=list(range(1,n))
            res_b=list(range(n,min(arr)))
            print(len(res_b)*len(res_f)+len(res_b)-1)
            sys.exit()

