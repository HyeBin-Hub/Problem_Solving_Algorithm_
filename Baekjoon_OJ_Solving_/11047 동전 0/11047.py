import sys

n, k = map(int,sys.stdin.readline().split())

arr = sorted([int(sys.stdin.readline()) for _ in range(n)],reverse=True)

total_count = 0

for num in arr:
    if k >= num : 
        count = k // num 
        k -= num * count
        total_count += count
        if k==0:
            break

print(total_count)

# [반례 1]
# 5 10
# 1
# 2
# 4
# 8
# 16

# [반례 2]
# 2 2
# 1
# 2



