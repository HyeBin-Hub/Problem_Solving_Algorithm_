n=int(input())
arr=[float(input())for _ in range(n)]
dp=[0.0]
for i in range(n):
    dp.append(max(dp[i]*arr[i],arr[i]))
print("{:.3f}".format(max(dp)))