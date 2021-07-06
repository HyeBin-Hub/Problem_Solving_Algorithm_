import sys
input=sys.stdin.readline
def primes(a,b):
    arr=[True]*(123456*2+1)
    count=0
    for i in range(2,int(b**0.5)+1):
        if arr[i]:
            for j in range(i*i,b+1,i):
                arr[j]=False
    for i in range(a+1,b+1):
        if arr[i]:
            count+=1
    return count
while 1:
    n=int(input())
    if n==0:
        break
    
    print(primes(n,2*n))