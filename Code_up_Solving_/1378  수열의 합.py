"""
# 1
n=int(input())
total=0
arr=[]
for i in range(1,n+1):
    arr.append(i)
    total+=sum(arr)
print(total)
""" 

# 2
n=int(input())
result=0
a=0
for i in range(1,n+1):
    a+=i
    result+=a
print(result)
