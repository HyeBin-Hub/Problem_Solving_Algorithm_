from itertools import permutations
import sys
n=int(sys.stdin.readline())
for i in list(permutations(range(1,n+1),n)):
    print(" ".join(map(str,i)))