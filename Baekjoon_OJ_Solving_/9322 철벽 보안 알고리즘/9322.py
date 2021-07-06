import sys
input=sys.stdin.readline
for i in range(int(input())):
    _=int(input())
    a=input().rstrip().split()
    b=input().rstrip().split()
    s=input().rstrip().split()
    r={ a.index(j):s[ind] for ind,j in enumerate(b)}
    for i in sorted(r.items(),key=lambda x:x[0]):
        print(i[1],end=" ")
    print()
