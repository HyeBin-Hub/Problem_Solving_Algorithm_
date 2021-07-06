from sys import stdin
input=stdin.readline
n,m=map(int,input().split())
def abc(n,m):
    s=[False,False]+[True]*(m-1)
    for i in range(2,int(m**0.5)+1):
        if s[i]:
            for j in range(2*i,m+1,i):
                s[j]=False
    for i in range(n,m+1):
        if i>1:
            if s[i]:
                print(i)
abc(n,m)