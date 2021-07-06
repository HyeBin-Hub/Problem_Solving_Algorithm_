import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
sum=0
for i in arr:
    sum+=i/max(arr)*100
print(round(sum/n,2))