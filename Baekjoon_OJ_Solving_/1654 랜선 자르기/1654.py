k,n=map(int,input().split())
arr=[int(input())for _ in range(k)]
left=1
right=max(arr)

while left<=right:
    mid=(left+right)//2
    res=[]
    lines=0
    for i in arr:
        lines+=i//mid

    if lines<n:
        right=mid-1
    elif lines>=n:
        left=mid+1

print(right)

