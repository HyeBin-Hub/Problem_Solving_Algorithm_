n,m=map(int,input().split())
arr=list(range(1,n+1))
count=0
for i in map(int,input().split()):
    ind=arr.index(i)
    count+=min(len(arr[ind:]),len(arr[:ind]))
    arr=arr[ind+1:]+arr[:ind]
print(count)