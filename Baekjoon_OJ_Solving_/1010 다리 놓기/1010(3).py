t=int(input())
dp=[]
dp.append(1)
dp.append(1)
for i in range(2,31):
    dp.append(i*dp[-1])
 
for _ in range(t):
    n,m=map(int,input().split())
    print(dp[m]//(dp[m-n]*dp[n]))
