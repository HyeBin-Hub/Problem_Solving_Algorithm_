from collections import deque
n,m=map(int,input().split())
arr=list(map(int,input().split()))
deq=deque(list(range(1,n+1)))
count=0
for i in arr:
    if len(deq)==1:
        continue
    
    if 0<=deq.index(i)<=len(deq)//2:
        count+=deq.index(i)
        deq.rotate(-deq.index(i))
        deq.popleft()
        
    else:
        count+=(len(deq)-deq.index(i))
        deq.rotate(len(deq)-deq.index(i))
        deq.popleft()        

print(count)

