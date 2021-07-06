n=int(input())
"""
#1

for i in range(n-1,-1,-1):
    for j in range(i):
        print(" ",end="")
    for j in range(1):
        print("*",end="")
    for j in range((n-i-1)*2):
        print(" ",end="")
    for j in range(1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(1):
        print("*",end="")
    for j in range((n-i-1)*2):
        print(" ",end="")
    for j in range(1):
        print("*",end="")
    print()

"""
#2

for i in range(n-1,-1,-1):
    for j in range(i):
        print(" ",end="")
    print("*",end="")
    for j in range((n-i-1)*2):
        print(" ",end="")
    print("*")

for i in range(n):
    for j in range(i):
        print(" ",end="")
    print("*",end="")
    for j in range((n-i-1)*2):
        print(" ",end="")
    print("*")

















    

