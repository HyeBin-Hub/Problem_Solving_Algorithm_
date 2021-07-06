n=int(input())
s=list(map(int,input().split()))
sum=0
for i in s:
    if i%5==0:
        sum+=i
print(sum)
