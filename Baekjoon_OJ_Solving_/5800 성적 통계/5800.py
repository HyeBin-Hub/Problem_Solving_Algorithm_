import sys
input=sys.stdin.readline
k=int(input())
for i in range(k):
    arr=list(map(int,input().split()))
    n,score=arr[0],sorted(arr[1:],key=lambda x:-x)
    print("Class {}".format(i+1))
    total=0
    for ind,j in enumerate(range(n-1)):
        a=score[ind]-score[j+1]
        if a>total:
            total=a
    print("Max {}, Min {}, Largest gap {}".format(score[0],score[-1],total))
    
