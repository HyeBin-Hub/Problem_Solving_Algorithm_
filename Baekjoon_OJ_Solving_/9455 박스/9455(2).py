t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    arr=[[*map(int,input().split())]for _ in range(n)]

    res=0

    for col in range(m):
        space_cnt=0
        for row in range(n-1,-1,-1):
            if arr[row][col]:
                res+=space_cnt
            else:
                space_cnt+=1
    print(res)