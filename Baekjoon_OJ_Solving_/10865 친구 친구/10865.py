import sys
input=sys.stdin.readline
def run():
    n,m=map(int,input().split())
    friends=[0]*(n+1)
    for i in range(m):
        a,b=map(int,input().split())
        friends[a]+=1
        friends[b]+=1
    print("\n".join(map(str,friends[1:])))
run()