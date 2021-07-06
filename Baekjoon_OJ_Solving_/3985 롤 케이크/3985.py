l=int(input())
n=int(input())
res1={}
arr=[0]*(l+1)
for i in range(1,n+1):
    p,k=map(int,input().split())
    res1[i]=k-p
    for j in range(p,k+1):
        if not arr[j]:
            arr[j]=i
print(sorted(res1.items(),key=lambda x:(-x[1],x[0]))[0][0])
maxs={}
for i in list(set(arr))[1:]:
    maxs[i]=arr.count(i)
print(sorted(maxs.items(),key=lambda x:-x[1])[0][0])

