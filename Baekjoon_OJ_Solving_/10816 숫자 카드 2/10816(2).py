import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))

arr_s=set(arr)

from collections import Counter
arr_c=Counter(arr)

for i in arr2:
    if i in arr_s :
        print(arr_c[i],end=" ")
    else:
        print(0,end=" ")