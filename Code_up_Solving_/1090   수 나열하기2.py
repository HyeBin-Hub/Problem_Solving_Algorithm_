# 1번째 방법
a,r,n=map(int,input().split())
print(a*r**(n-1))

# 2번째 방법

a,r,n=map(int,input().split())
for i in range(n-1):
    a*=r
print(a)
