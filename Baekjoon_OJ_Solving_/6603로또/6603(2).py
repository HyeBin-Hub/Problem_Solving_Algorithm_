from itertools import combinations
import sys
input=sys.stdin.readline
while 1:
    arr=list(map(int,input().split()))
    if arr==[0]:
        break
    res=sorted(list(combinations(arr[1:],6)))
    for i in res:
        print(" ".join(map(str,i)))
    print()
    