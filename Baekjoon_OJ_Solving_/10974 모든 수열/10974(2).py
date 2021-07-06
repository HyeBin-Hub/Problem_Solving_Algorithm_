import sys
input=sys.stdin.readline
def run(save):
    if len(save)==n:
        print(*save)
        return
    
    for i in range(1,n+1):
        if i not in save:
            run(save+[i])
n=int(input())
run([])