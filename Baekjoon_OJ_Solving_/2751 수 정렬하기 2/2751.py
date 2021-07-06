import sys
input=sys.stdin.readline
n=int(input())
print("\n".join(map(str,sorted([int(input()) for i in range(n)]))))