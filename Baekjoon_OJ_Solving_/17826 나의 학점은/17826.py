from bisect import bisect_left
a=list(map(int,input().split()))
me=int(input())
arr=[5,15,30,35,45,48,50]
res=["A+","A0","B+","B0","C+","C0","F"]
print(res[bisect_left(arr,a.index(me)+1)])