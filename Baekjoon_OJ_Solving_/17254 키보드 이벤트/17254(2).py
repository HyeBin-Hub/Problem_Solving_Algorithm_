n,m=map(int,input().split())
arr=[list(input().rstrip().split())for _ in range(m)]
a=sorted(arr,key=lambda x:(int(x[1]),int(x[0])))
res=""
for i in a:
    res+=i[2]
print(res)