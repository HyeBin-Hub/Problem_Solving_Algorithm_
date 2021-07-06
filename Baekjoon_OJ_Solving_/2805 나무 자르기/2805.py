from collections import Counter
import sys
input=sys.stdin.readline
def run():
    n,m=map(int,input().split())
    dic={}
    for i in map(int,input().split()):
        dic[i]=dic.get(i,0)+1

    left=0
    right=max(dic)
    while left<=right:

        mid=(left+right)//2

        total=0
        for k,v in dic.items():
            if mid<k:
                total+=(k-mid)*v

        if total>=m:
            dicult=mid
            left=mid+1
        else:
            right=mid-1
    print(dicult)
run()