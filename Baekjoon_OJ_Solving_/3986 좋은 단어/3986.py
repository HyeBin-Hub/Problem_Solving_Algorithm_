import sys
input=sys.stdin.readline
n=int(input())
count=0
for _ in range(n):
    s=list(input().rstrip())
    res=[]
    
    for i in s:
        if not res:
            res.append(i)
        else:
            if res[-1]==i:
                res.pop()
            else:
                res.append(i)
    if not res:
        count+=1

            
print(count) 