# 정답은 아닌대 내가 푼 방법

n=int(input())
arr=[]
for i in range(2,n):
    if n%i==0:
        arr.append(i)
a=arr[-1]
count=0
for i in range(arr[-1]):
    if a%i==0:
        count+=0
    else:
        count+=1
        
if count<=2:
    print(arr[0],arr[-1])
else:
    print("wrong number")

# 다른 사람 정답

import math
​
n = int(input())
a = []
index = 0
sq = int(math.sqrt(float(n)))
​
for i in range(0, 30):
    a.append(0)
​
for i in range(2, sq+1):
    while n % i == 0:
        n /= i
        a[index] = i
        index += 1
​
if n != 1:
    a[index] = n
    index += 1
if index == 2:
    print(int(a[0]), int(a[1]))
else:
    print('wrong number')
