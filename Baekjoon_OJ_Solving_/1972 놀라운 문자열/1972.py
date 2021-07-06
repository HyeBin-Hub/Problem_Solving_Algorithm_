import sys
while 1:
    s=list(input().rstrip())
    
    if s==["*"]:
        sys.exit()

    if len(s)==1:
        print("{} is surprising.".format(s[0]))
        continue

    else:
        flag=0
        for i in range(1,len(s)):
            res=[] # 각각의 D-쌍 담을 리스트
            for j in range(len(s)-i):
                if s[j]+s[j+i] not in res:  
                    res.append(s[j]+s[j+i])
                else:
                    flag=1 # not surprising
        if flag:
            print("{} is NOT surprising.".format("".join(s)))
        else:
            print("{} is surprising.".format("".join(s)))


                 
                


        