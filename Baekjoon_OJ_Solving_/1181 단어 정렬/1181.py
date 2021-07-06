import sys
input=sys.stdin.readline
n=int(input())
arr=sorted(set([input().rstrip() for _ in range(n)]),
           key=lambda x:(len(x),x))
sys.stdout.write("\n".join(i for i in arr))