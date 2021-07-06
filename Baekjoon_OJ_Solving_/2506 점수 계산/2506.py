n=int(input())
s=list(map(int,input().split()))
sum,num=0,0
for i in s:
    if i==1:
        num+=1
        sum+=num
    else:
        num=0
print(sum)