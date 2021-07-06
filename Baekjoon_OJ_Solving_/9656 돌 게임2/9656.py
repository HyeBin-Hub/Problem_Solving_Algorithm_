import sys
input=sys.stdin.readline
n=int(input())

dp=[1]*1001
dp[1]=0
dp[2]=1
dp[3]=0

for i in range(4,1001):
    if dp[i-1]==dp[i-3]==1:
        dp[i]=0
print(["CY","SK"][dp[n]])