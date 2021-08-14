n=int(input())
arr=[list(map(int,input().split()))for _ in range(n)]
res=sorted(arr,key=lambda x:(x[1],x[0]))
print(" ".join(str(res)))
