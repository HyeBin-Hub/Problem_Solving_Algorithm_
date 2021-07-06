"""
#2-1
n=int(input())
for i in range(n):
    if i%2!=0:
        for j in range(n,0,-1):
            print(n*i+j,end=" ")
    else:
        for j in range(1,n+1):
            print(n*i+j,end=" ")
    print()
"""
"""
#2-2
n=int(input())
for i in range(n):
    if i==0 or i%2==0:
        for j in range(n,0,-1):
            print(n*i+j,end=" ")
    else:
        for j in range(1,n+1):
            print(n*i+j,end=" ")
    print()
"""
#2-3
n=int(input())
a=[[0]*n for i in range(n)]
#[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
cut=0
for i in range(n):
    if i%2:
        for j in range(n-1,-1,-1):
            cut+=1
            a[i][j]=cut

















