n=int(input())
arr=[list(map(int,input().split()))for i in range(n)]
res=sorted(arr,key=lambda x:(x[0],x[1]))
for i in res:
    print(i[0],i[1])