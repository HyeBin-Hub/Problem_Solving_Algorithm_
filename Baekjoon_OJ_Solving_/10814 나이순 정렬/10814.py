import sys
n = int(sys.stdin.readline())
li = sorted([sys.stdin.readline() for _ in range(n)], key=lambda x: int(x.split()[0]))
for k in li :
    sys.stdout.write(k)