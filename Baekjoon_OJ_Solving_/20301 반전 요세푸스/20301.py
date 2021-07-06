from collections import deque
n,k,m=map(int,input().split())

arr=deque(list(range(k,n+1))+list(range(1,k)))

count=1
while arr:
    if (count//m)%2==0:
        print(arr.popleft())
        arr.rotate(-(k-1))
   
    else:
        print(arr.popleft())
        arr.rotate(k)

    count+=1
    




