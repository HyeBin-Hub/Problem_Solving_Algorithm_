import sys
input=sys.stdin.readline
n=int(input())
s=input().rstrip()
if s.count("LL")>0:
    print(len(s.replace("LL","S"))+1)
else:
    print(n)