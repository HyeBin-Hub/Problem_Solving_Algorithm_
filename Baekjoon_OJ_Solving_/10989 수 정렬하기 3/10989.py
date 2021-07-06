import sys
input=sys.stdin.readline
def sort(n):
    arr=[0]*10001
    for i in range(n):
        p=int(input())
        arr[p]+=1
    for ind,cou in enumerate(arr):
        for j in range(cou):
            print(ind)

   
sort(int(input()))