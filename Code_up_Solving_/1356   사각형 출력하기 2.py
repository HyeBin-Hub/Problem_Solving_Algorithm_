n=int(input())
for i in range(n):
    if i==0 or i==n-1:
        for j in range(n):
            print("*",end="")
        print()
    else:
        print("*",end="")
        for j in range(n-2):
            print(" ",end="")
        print("*",end="")
        print()
