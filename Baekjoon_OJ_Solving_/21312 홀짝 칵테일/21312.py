import sys
input=sys.stdin.readline
arr=list(map(int,input().split()))
odd=[]
even=[]
for i in arr:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
if not odd:
    res=1
    for i in even:
        res*=i
    print(res)
else:
    res=1
    for i in odd:   
        res*=i
    print(res)