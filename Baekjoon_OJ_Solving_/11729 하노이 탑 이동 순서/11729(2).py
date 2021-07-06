def run(n,start,t,mid):
    if n==1:
        print(start,t)
        return
    run(n-1,start,mid,t)
    print(start,t)
    run(n-1,mid,t,start)

n=int(input())

result=1
for _ in range(n-1):
    result = result * 2 + 1
print(result)

run(n,1,3,2)
