t=int(input())
for i in range(1,t+1):
    n=int(input())
    arr=list(map(int,input().split()))

    while len(arr)!=2:
        res=[arr[0]+arr[-1]]
        for j in range(len(arr)//2):
            res.append(arr[j+1]+arr[-2-j])
        arr=res
     
    if arr[0]>arr[1]:
        print("Case #{}: Alice".format(i))
    else:
        print("Case #{}: Bob".format(i))




    
    
    