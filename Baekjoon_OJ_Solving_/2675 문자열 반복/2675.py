n=int(input())
while n!=0:
    n-=1
    a,b=input().split()
    for i in b:
        for j in range(int(a)):
            print(i,end="")
    print()