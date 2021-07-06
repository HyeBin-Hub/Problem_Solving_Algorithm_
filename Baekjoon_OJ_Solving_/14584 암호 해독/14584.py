import sys
input=sys.stdin.readline
s=input().rstrip()
n=int(input())
arr=[input().rstrip() for _ in range(n)]

while 1:
    for i in arr:
        if i in s:
            print(s)
            sys.exit()

    res=""
    for ch in s:
        c=ord(ch)+1
        if c>122:
            c=97

        res+=chr(c)
    s=res
print(s)