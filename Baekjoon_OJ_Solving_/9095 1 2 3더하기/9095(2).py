t=int(input())
dp=[0]*11
for i in range(1,11):
    if i in (1,2,3):
        dp[i]+=1
    dp[i]+=dp[i-1]
    if i>1:
        dp[i]+=dp[i-2]
    if i>2:
        dp[i]+=dp[i-3]
for i in range(t):
    n=int(input())
    print(dp[n])

