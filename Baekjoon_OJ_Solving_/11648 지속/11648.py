n=list(input().rstrip())

count=0
a=1
while len(n)!=1:
    for i in n:
        i=int(i)
        a*=i
        
    n=list(str(a))
    count+=1
    a=1
print(count)
