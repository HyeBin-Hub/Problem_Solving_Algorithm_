n=int(input())
s=list(map(int,input().split()))
count=0
for i in range(n):
    count+=1
    if i==max(s):
        print(i)
print(count)
        
