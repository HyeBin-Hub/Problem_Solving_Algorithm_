
from itertools import permutations
n=int(input())
arr=list(map(int,input().split()))
res=[]
for i in list(permutations(arr,n)):
    total=0
    for j in range(n-1):
        total+=abs(i[j]-i[j+1])
    res.append(total)
print(max(res))

