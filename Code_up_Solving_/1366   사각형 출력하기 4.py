n=int(input())
for i in range(n):
    print("*",end="")
print()

for i in range(1,n-2):
    for j in range(n):
        if j==0 or j==n-1 or j==n//2 or j==i or j==n-i-1 or i==n//2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
            
    
for i in range(n):
    print("*",end="")
print()
