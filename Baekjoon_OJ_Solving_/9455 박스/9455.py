t=int(input())
for  _ in range(t):
    n,m=map(int,input().split())
    arr=[list(map(int,input().split()))for _ in range(n)]
    total_cnt=0
    for col in range(m):
        space_cnt=0
        for row in range(n):
            if arr[row][col] ==0:
                    continue
            else:
                for i in range(row+1,n):
                    if arr[i][col]==0:
                        space_cnt+=1
        total_cnt+=space_cnt
    print(total_cnt)
            
            



        