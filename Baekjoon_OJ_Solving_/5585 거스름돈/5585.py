arr=[500,100,50,10,5,1]
n=int(input())
p=1000-n
count=0
for i in arr:
    if p>=i:
        count+=p//i
        p=p%i
print(count)