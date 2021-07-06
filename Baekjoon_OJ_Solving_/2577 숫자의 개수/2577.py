from sys import stdin,stdout
from collections import Counter
input=stdin.readline
print=stdout.write
a=int(input())
b=int(input())
c=int(input())
arr=str(a*b*c)
res=Counter(arr)
t=[0]*10
for k,v in res.items():
    t[int(k)]=v
print("\n".join(map(str,t)))