n=int(input())
answer=0
left=1
right=n
while left<=right:
    mid=(left+right)//2
    if mid*(mid+1)//2 <=n:
        answer=mid
        left=mid+1
    else:
        right=mid-1
print(answer)