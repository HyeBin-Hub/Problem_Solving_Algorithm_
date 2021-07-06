import sys
input=sys.stdin.readline
def run(save):
    if len(save)==m:
        print(*save)
        return
    for i in range(n):
        save.append(arr[i])
        run(save)
        save.pop()

n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
save=[]
run(save)