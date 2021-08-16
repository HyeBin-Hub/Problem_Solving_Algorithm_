n=int(input())
a=sorted(list(map(int,input().split())))
b=sorted(list(map(int,input().split())),reverse=True)
total=0
for i,j in zip(a,b):
    total+=i*j
print(total)