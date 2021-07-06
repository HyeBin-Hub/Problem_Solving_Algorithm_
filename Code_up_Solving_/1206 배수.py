a,b=map(int,input().split())
if a%b==0:
    c=a//b
    print("{}*{}={}".format(b,c,a))
elif b%a==0:
    c=b//a
    print("{}*{}={}".format(a,c,b))
else:
    print("none")
    
    
