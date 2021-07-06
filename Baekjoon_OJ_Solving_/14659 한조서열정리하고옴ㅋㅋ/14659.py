import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
r=0 
count=0
arr=[]
for i in a:
    if r<i:
        r=i
        arr.append(count)
        count=0
    else:
        count+=1
arr.append(count)
print(max(arr))
