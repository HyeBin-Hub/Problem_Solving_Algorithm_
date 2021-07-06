import sys
input = sys.stdin.readline
print = sys.stdout.write
n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
print("\n".join(map(str,sorted(arr))))