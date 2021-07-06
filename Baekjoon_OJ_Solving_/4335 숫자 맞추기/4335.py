res=[]

while 1:
    n=int(input())
    if n==0:
        break
    s=input().rstrip()
    if s!="right on":
        res.append([n,s])
    else:

        flag=0
        for i in res:
            if n < i[0] and i[1]=="too low" : 
                flag=1 # 틀림
                break
            elif n > i[0] and i[1]=="too high":
                flag=1 # 틀림
                break
        if flag:
            print("Stan is dishonest")
        else:
            print("Stan may be honest")
        res=[]


    