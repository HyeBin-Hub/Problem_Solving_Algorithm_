n=num=int(input())
count=0
while 1:
    a=n//10+n%10
    n=(n%10)*10+a%10
    count+=1
    if n==num:
        break
print(count)