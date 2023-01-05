import sys

_, _ = map(int,sys.stdin.readline().split())
res = []
a = [*map(int,sys.stdin.readline().split())]
b = [*map(int,sys.stdin.readline().split())]
arr = a+b
print(sorted(arr))

# --------------------------------------------

for _ in range(2):
    arr = [*map(int,sys.stdin.readline().split())]
    res.extend(arr)
print(*sorted(res))

# ---------------------------------------------

import sys

_,_ = sys.stdin.readline().split()
print(" ".join(sorted(sys.stdin.read().split(),key=int)))