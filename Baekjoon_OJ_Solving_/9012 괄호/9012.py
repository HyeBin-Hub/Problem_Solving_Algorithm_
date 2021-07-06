import sys
input=sys.stdin.readline
n=int(input())
for _ in range(n):
    s=input().rstrip()
    res=[]
    for i in s:
        if not res:
            res.append(i)
        else:
            if res[-1]=="(" and i==")":
                res.pop()
            elif res[-1]=="(" and i=="(":
                res.append(i)
    if not res:
        print("YES")
    else:
        print("NO")