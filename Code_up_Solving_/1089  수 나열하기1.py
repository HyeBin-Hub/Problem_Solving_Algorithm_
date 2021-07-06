# 1번째 방법

a,d,n=map(int,input().split())
arr=[]
for i in range(n):
    a+=d
    arr.append(a)
print(arr[n-2])

# 2 번째 방법

a,d,n=map(int,input().split())
print(a+d*(n-1))

# 3 번째 방법

a,d,n=map(int,input().split())
for i in range(n-1):
    a+=d
print(a)
