import math
n=int(input())
for i in range(1,n):
    if math.sqrt(n-i)%1==0:
        k=i
        a=int(math.sqrt(n-i))
        break
print(k,a)
