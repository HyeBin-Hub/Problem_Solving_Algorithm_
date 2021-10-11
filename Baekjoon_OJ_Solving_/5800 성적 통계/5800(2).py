import sys
input=sys.stdin.readline
k=int(input())
for i in range(k):
    n,*score=list(map(int,input().split()))
    score=sorted(score,key=lambda x:-x)
    print("Class {}".format(i+1))
    total=0
    for j in range(n-1):
        a=score[j]-score[j+1]
        if a>total:
            total=a
    print("Max {}, Min {}, Largest gap {}".format(score[0],score[-1],total))
    
