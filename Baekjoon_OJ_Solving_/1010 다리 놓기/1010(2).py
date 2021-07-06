t=int(input())
dp=[0]*31
dp[0]=1
dp[1]=1
for i in range(2,31):
    dp[i]+=dp[i-1]*i

for _ in range(t):
    n,m=map(int,input().split())
    print(dp[m]//(dp[m-n]*dp[n]))

