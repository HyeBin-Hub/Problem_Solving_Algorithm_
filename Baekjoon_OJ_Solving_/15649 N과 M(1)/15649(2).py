from itertools import permutations
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=list(map(str,range(1,1+n)))
print('\n'.join(list(map(' '.join,permutations(arr, m)))))
