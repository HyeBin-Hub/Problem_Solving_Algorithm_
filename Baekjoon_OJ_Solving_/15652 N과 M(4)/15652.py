import sys
input=sys.stdin.readline
def run(index,save):
    if len(save)==m:
        print(*save)
        return
    for i in range(index,n+1):
        save.append(i)
        run(i,save)
        save.pop()


n,m=map(int,input().split())
save=[]
index=1
run(index,save)