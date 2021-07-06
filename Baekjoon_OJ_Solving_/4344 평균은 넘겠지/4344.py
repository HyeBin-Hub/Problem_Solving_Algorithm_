import sys
input=sys.stdin.readline
c=int(input())
for i in range(c):
    arr=list(map(int,input().split()))
    avg=sum(arr[1:])/arr[0]
    count=0
    for i in arr[1:]:
        if avg<i:
            count+=1
    parsent=(count/arr[0])*100
    print("{:.3f}%".format(round(parsent,3)))