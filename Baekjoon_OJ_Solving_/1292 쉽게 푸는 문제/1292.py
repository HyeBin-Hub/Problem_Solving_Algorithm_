
a,b=map(int,input().split())

res=[]
for i in range(1,46):
    res+=[i]*i

print(sum(res[a-1:b]))
