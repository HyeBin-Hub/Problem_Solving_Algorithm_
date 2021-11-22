import sys
input=sys.stdin.readline
while 1:
    n=int(input())
    if n==0:
        break
    d={}
    for i in range(n):
        a=input().rstrip()
        d[a.lower()]=a
    d=sorted(d.items(),key=lambda x:x[0])
    print(d[0][1])
    

