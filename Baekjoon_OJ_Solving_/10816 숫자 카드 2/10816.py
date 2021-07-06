

import sys
input=sys.stdin.readline
from collections import Counter

_=int(input())
arr=Counter(input().rstrip().split())
_=int(input())
arr2=input().rstrip().split()
print(" ".join (str(arr[i]) if i in arr else "0" for i in arr2))