import sys
input=sys.stdin.readline

n=int(input())
for i in range(n):
    a=int(input())
    num=10
    while num<a:
        if a%num>=5*num*0.1:
            a=a+(num-a%num)
        else:
            a=a-a%num
        num*=10
    print(a)
