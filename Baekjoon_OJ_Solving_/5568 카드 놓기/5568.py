import sys
input=sys.stdin.readline
from itertools import permutations
n=int(input())
k=int(input())
arr=[input().rstrip()for _ in range(n)]
a=list(permutations(arr,k))
print(len(set([int("".join(i))for i in a])))