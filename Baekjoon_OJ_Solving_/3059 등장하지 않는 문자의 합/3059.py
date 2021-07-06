import sys
input=sys.stdin.readline
n=int(input())
for _ in range(n):
    s=input().rstrip()
    count=0
    for i in range(65,91):
        if chr(i) not in s:
            count+=i
    print(count)