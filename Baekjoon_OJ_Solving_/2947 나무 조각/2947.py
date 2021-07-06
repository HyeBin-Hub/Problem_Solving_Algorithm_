

arr=list(map(int,input().split()))

while 1:
    for i in range(1,len(arr)-1):
        if arr[i]<arr[i-1]:
            arr[i-1],arr[i]=arr[i],arr[i-1]
        elif arr[i]>arr[i-1]:
            continue    
        print(arr)
    if arr==[1,2,3,4,5]:
        break
