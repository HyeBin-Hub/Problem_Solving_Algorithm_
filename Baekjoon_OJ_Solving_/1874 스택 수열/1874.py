
import sys
input=sys.stdin.readline
n=int(input())

last=0

arr=[int(input())for _ in range(n)]

stack=[]
res=[]

for i in arr:

    if not stack:
        stack.extend(list(range(last+1,i+1)))
        res.extend(list("+"*len(stack)))
        last=i

    if stack[-1]==i:
        stack.pop()
        res.extend("-")

    elif stack[-1]<i:
        stack.extend(range(last+1,i+1))
        res.extend(len(list(range(last+1,i+1)))*"+")
        last=i
        stack.pop()
        res.extend("-")
    else:
        break
    
if stack:
    print("NO")
else:
    print("\n".join(res))


