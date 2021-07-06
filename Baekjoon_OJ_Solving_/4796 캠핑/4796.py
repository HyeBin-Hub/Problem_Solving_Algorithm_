cnt=1
while 1:
    l,p,v=map(int,input().split())
    
    if l==p==v==0:
        break
    a,b=divmod(v,p)
    if b<=l:
        print("Case {}: {}".format(cnt,a*l+b))
    else:
        print("Case {}: {}".format(cnt,a*l+l))
    cnt+=1
 