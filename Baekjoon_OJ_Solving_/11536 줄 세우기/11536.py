import sys
input=sys.stdin.readline
n=int(input())
s=[input() for _ in range(n)]


if s==sorted(s): 
    print("INCREASING")
elif s==sorted(s,reverse=True):
    print("DECREASING")
else:
    print("NEITHER")
