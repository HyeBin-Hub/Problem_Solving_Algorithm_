n,t=map(int,input().split())
s=list(map(int,input().split()))
total,count=0,0
for i in s:
    total+=i
    if total<=t:
        count+=1
print(count)