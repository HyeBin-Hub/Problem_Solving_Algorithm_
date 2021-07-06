from collections import deque
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))

    res=deque(arr)
    serial_number=deque(list(range(n)))
    prints=[]
    

    while serial_number:
        r=res.index(max(res))
        res.rotate(-r)
        serial_number.rotate(-r)
        a=res.popleft()
        b=serial_number.popleft()
        prints.append(b)
        while 1:
            if not res:
                break
            if a==res[0]:
                res.popleft()
                v=serial_number.popleft()
                prints.append(v)
            else:
                break
    print(prints.index(m)+1)