h,k,d=input().split()
h=int(h)
k=int(k)
for i in range(h):
    if d=="L":
        for j in range(i):
            print(" ",end="")
        for j in range(k):
            print("*",end="")
        print()
    elif d=="R":
        for j in range(h-i-1):
            print(" ",end="")
        for j in range(k):
            print("*",end="")
        print()
