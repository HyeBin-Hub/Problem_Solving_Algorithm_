import sys
input=sys.stdin.readline
def run(index,save):
    if len(save)==m:
        print(*save)
        return
    for i in range(index,n):
        save.append(arr[i])
        run(i,save)
        save.pop()


n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
save=[]
index=0
run(index,save)