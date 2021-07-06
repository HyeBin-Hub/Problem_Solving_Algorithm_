from math import sqrt
def prime():
    # 소수 True로 표시
    arr=[False,False]+[True]*999999
 
    for i in range(4,999999,2):
        arr[i]=False

    for i in range(3,int(sqrt(999999))+1,2):
        if arr[i]:
            for j in range(i*2,999999,i):
                arr[j]=False

    while 1:
        n=int(input())
        if not n:
            break
        for i in range(2,n):
            if arr[i] and arr[n-i]:
                print("{} = {} + {}".format(n,i,n-i))
                break
                
    
prime()
