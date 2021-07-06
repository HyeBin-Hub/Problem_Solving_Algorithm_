import sys

input=sys.stdin.readline
def run(index,arr,save):
    if len(save)==6:
        print(*save)
        return
    
    for i in range(index,len(arr)):
        if arr[i] not in save:
            save.append(arr[i])
            run(i,arr,save)
            save.pop()
            
while 1:
    arr=list(map(int,input().split()))
    if arr==[0]:
        break
    save=[]
    run(0,arr[1:],save)
    print()