a,b=map(int,input().split())
z=0
def get(n):
    for i in range(1,n+1):
        if i%2==0:
            q=int(i/2)*10
        else:
            q=int(i/2)+1
    return q
z+=get(a)
z+=get(b)
print(z)
