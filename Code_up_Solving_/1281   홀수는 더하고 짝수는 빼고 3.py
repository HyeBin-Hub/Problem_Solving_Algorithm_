a,b=map(int,input().split())
sum=0
for i in range(a,b+1):
    if i%2==0 :
        sum-=i
        print("-"+str(i),end="")
    else:
        if i==a:
            print(str(i),end="")
        else:
            print("+"+str(i),end="")
        sum+=i
        
if sum>0:
    print("=+"+str(sum))
else:
    print("="+str(sum))
        
