import sys
input=sys.stdin.readline
n=int(input())
stu_so=sorted([input().rstrip().split() for _ in range(n)],
              key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))
print("\n".join(i[0] for i in stu_so))