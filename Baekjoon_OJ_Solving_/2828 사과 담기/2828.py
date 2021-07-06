import sys
input=sys.stdin.readline
n,m=map(int,input().split())
j=int(input())
count=0
left=1
right=m
for _ in range(j):
    fall_apple=int(input()) 
    if left<=fall_apple<=right:
        continue
    if fall_apple>right:
        count+=(fall_apple-right)
        left+=(fall_apple-right)
        right+=(fall_apple-right)
        
    elif fall_apple<left:
        count+=(left-fall_apple)
        right-=(left-fall_apple)
        left-=(left-fall_apple)
        
print(count)

# left, right 위치 지정잘하기
# 아님 먼저 떨어진 사과랑 왼쪽 오른쪽 거리 계산해주기