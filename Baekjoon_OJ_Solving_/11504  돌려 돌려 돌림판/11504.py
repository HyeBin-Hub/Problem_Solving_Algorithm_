t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    x=int("".join(map(str,list(map(int,input().split())))))
    y=int("".join(map(str,list(map(int,input().split())))))
    arr=list(input().split())
    arr=arr+arr[:m-1]
    count=0
    for i in range(n):
        res=int("".join(arr[i:m+i]))
        if x<=res<=y:
            count+=1
    print(count)
        
    
    


