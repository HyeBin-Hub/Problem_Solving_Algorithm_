import sys
input=sys.stdin.readline
n=int(input())
que=[]
for i in range(n):
    s=input().split()
    if s[0]=="push":
        que.insert(0,int(s[1]))
    elif s[0]=="pop":
        if len(que)!=0: 
            print(que.pop())
        else:
            print(-1)
    elif s[0]=="size":
        print(len(que))
    elif s[0]=="empty":
        if len(que)!=0: 
            print(0)
        else:
            print(1)
    elif s[0]=="front":
        if len(que)!=0:
            print(que[-1])
        else:
            print(-1)
    elif s[0]=="back":
        if len(que)!=0:
            print(que[0])
        else:
            print(-1)