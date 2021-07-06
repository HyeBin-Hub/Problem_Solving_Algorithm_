"""
#1-1
n=int(input())
for i in range(n):
    for j in range(1,n+1):
        print(n*i+j,end=" ")
    print()
"""
"""
#1-2
n=int(input())
for i in range(n):
    for j in range(n,0,-1):
        print(n*i+j,end=" ")
    print()
"""
"""
#1-3
n=int(input())
for i in range(1,n+1):
    for j in range(n):
        print(n*j+i,end=" ")
    print()
"""
"""
#1-4
n=int(input())
for i in range(n,0,-1):
    for j in range(n):
        print(n*j+i,end=" ")
    print()
"""
"""
#1-5
n,m=map(int,input().split())
for i in range(n-1,-1,-1):
    for j in range(m,0,-1):
        print(m*i+j,end=" ")
    print()
"""
"""
#1-6
n,m=map(int,input().split())
for i in range(n-1,-1,-1):
    for j in range(1,m+1):
        print(m*i+j,end=" ")
    print()
"""
"""
#1-7
n,m=map(int,input().split())
for i in range(n,0,-1):
    for j in range(m-1,-1,-1):
        print(n*j+i,end=" ")
    print()
"""
"""
#1-8
n,m=map(int,input().split())
for i in range(1,n+1):
    for j in range(m-1,-1,-1):
        print(n*j+i,end=" ")
    print()
"""



























