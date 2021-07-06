n=int(input())
arr=list(map(int,input().split()))
dp=[0]*1001
for i in arr:
    dp[i]=max(max(dp[:i])+i,dp[i])
print(max(dp))
