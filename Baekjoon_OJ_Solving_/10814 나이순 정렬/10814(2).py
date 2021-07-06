import sys
input=sys.stdin.readline
n=int(input())
arr=[input().rstrip().split()for _ in range(n)]
a=sorted(arr,key=lambda x:int(x[0]))
for i in a:
    print(i[0],i[1])