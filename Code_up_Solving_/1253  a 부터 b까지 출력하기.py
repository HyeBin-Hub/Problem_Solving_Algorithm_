a,b=map(int,input().split())
if a>b:# a가 b보다 클경우
    for i in range(b,a+1):
        print(i,end=" ")
else:
    for i in range(a,b+1):
        print(i,end=" ")
