def run():
    n,m=map(int,input().split())
    arr=[int(input())for _ in range(n)]
    left=max(arr)
    right=sum(arr)
    final=sum(arr)
    while left<=right:
        mid=(left+right)//2
        current_total=0
        patition=1
        for i in arr:
            current_total+=i
            if current_total>mid:
                patition+=1
                current_total=i
        if patition<=m:
            if mid<final:
                final=mid
            right=mid-1
        else:
            left=mid+1
    print(final)
run()
