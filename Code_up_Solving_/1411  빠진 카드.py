"""
n=int(input())
arr=[]
for i in range(n-1):
    a=int(input())
    arr.append(a)
    arr.sort()
arr.append(0)

arr2=[]
for i in range(1,n+1):
    arr2.append(i)
    
for i in range(n):
    if arr2[i]==arr[i]:
        pass
    else:
        print(arr2[i])
        break
"""

n=int(input())
arr=[]
arr2=[]
for i in range(1,n+1):
    arr.append(i)
#[1,2,3,4,5,6,7,8,9,10]
for i in range(n-1):
    a=int(input())
    arr2.append(a)

for i in arr2:
    arr.remove(i)
print(arr[0])
