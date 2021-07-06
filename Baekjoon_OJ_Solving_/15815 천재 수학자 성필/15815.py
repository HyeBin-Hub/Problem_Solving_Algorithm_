import sys
input=sys.stdin.readline
s=input().rstrip()
stack=[]
for i in s:
    if i=="+":
        stack.append(stack.pop()+stack.pop())
    elif i=="*":
        stack.append(stack.pop()*stack.pop())
    elif i=="/":
        a1=stack.pop()
        a2=stack.pop()
        stack.append(a2//a1)
    elif i=="-":
        a1=stack.pop()
        a2=stack.pop()
        stack.append(a2-a1)
    else:
        stack.append(int(i))
print(stack[0])