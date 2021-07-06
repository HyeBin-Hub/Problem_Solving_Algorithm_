n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
s=[[0]*n for _ in range(n)]
s[0][0]=1
for row in range(n):
    for col in range(n):
        if row ==n-1 and col==n-1:
            break
    
        # 아래로 이동
        if row+arr[row][col]<n:
            s[row+arr[row][col]][col]+=s[row][col]
        
        # 오른쪽으로 이동
        if col+arr[row][col]<n:
            s[row][col+arr[row][col]]+=s[row][col]


#print(["HaruHaru","Hing"][s[n-1][n-1]==0])
print("HaruHaru" if s[n-1][n-1] else "Hing")


