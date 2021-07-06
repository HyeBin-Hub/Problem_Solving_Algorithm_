n=int(input())
request=list(map(int,input().split()))
limit=int(input())

left=1
right=max(request)
while left<=right:
    mid=(left+right)//2
    total=0
    for i in request:
        if mid>i:
            total+=i
        else:
            total+=mid
    if total>limit:
        right=mid-1
    else:
        left=mid+1
print(right)