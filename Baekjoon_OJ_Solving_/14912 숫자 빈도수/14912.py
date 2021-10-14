import sys
input=sys.stdin.readline
n,d=map(int,input().split())
print("".join(map(str,range(1,n+1))).count(str(d)))


