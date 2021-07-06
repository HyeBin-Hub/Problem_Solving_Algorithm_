# 1번째 방법

n=int(input())
count=0
for i in range(1,n+1):
    if n%i!=0:
        count+=0
    else:
        count+=1
if count<=2:
    print("prime")
else: 
    print("not prime")

# 2번째 방법

n=int(input())
a="prime"
for i in range(2,n):
    if n%i==0:
        a="not prime"
        break
print(a)
