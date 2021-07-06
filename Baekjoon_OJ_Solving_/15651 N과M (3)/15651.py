import sys
input=sys.stdin.readline
def run(save):
    if len(save)==m:
        print(*save)
        return
    for i in range(1,n+1):
        save.append(i)
        run(save)
        save.pop()


n,m=map(int,input().split())
save=[]
run(save)