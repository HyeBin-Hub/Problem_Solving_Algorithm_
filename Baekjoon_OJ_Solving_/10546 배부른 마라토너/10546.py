def run():
    n=int(input())
    stack=[]
    for i in range(n):
        stack.append(input().rstrip())
    stack2=[]
    for i in range(n-1):
        stack2.append(input().rstrip())
    stack2.append("z"*20)
    for a,b in zip(sorted(stack),sorted(stack2)):
        if a!=b:
            print(a)
            break
run()