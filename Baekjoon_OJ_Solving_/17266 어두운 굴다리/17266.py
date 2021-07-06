n=int(input())
m=int(input())
arr=list(map(int,input().split()))

left=0
right=n

while 1:
    if right-left<=1:
        break

    mid=(left+right)//2

    flag=1 # 영역을 다 채웠다는 의미

    for i in range(1,m):
        # 가로등의 간격이 mid*2랑 같으면 겹치지 않고 영역 채움
        # 가로등의 간격이 mid*2보디 작으면 겹치면서 영역을 채움 
        if arr[i]-arr[i-1]>mid*2: 
            flag=0
            break
    
    if arr[0]>mid or n-arr[-1]>mid:
        flag=0

    if flag:
        right=mid
    else:
        left=mid
flag=1

for i in range(1,m):
    if arr[i]-arr[i-1]>left*2:
        flag=0
        break

if arr[0]>left or n-arr[-1]>left:
    flag=0

if flag:
    print(left)
else:
    print(right)

