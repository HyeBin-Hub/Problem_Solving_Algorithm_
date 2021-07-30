from collections import deque

n=int(input())
res=list(map(int,input().split()))
arr_num=deque(list(range(1,n+1)))
arr=deque(res)


q=[arr_num[0]]
while arr:
    a=arr.popleft()
    b=arr_num.popleft()
    if a<0:
        arr.rotate(-a)
        arr_num.rotate(-a)
    else:
        arr.rotate(a-1)
        arr_num.rotate(a-1)
    #print("arr : ",arr)
    if arr:
        q.append(arr_num[0])
print(*q)  

# # 1 5 3 2 4