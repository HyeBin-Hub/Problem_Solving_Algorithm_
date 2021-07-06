n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

arr.sort()

start_xi=arr[0][0]
start_yi=arr[0][1]
total_len=0

for i in arr[1:]:
    if start_xi <= i[0] <= start_yi and start_xi <= i[1] <= start_yi: # 한 라인에 다 포함되는 라인의 경우
        continue
    elif start_yi >= i[0]:
        start_yi=i[1]
    elif start_yi <i[0]:
        total_len+=start_yi-start_xi
        start_xi=i[0]
        start_yi=i[1]

total_len+=start_yi-start_xi
print(total_len)

