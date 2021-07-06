from itertools import product
import sys
input=sys.stdin.readline
arr=[1,2,3]
t=int(input())
for _ in range(t):
    n=int(input())
    count=0
    for i in range(1,n+1):  
        for j in list(product(arr,repeat=i)):
            if sum(j)==n:
                count+=1
    print(count)
