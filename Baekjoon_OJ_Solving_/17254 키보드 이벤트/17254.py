
n,m=map(int,input().split())
res=[]
for i in range(m):
    a,b,c=input().rstrip().split()
    res.append((int(b),int(a),c))
res.sort()
for i in res:
    print(i[2],end="")