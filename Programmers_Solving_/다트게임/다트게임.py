def solution(dartResult):
    for i in dartResult:
        global res
        if i=="S":
            res[-1]=res[-1]**1
        elif i=="D":
            res[-1]=res[-1]**2
        elif i=="T":
            res[-1]=res[-1]**3
        elif i=="*": 
            res[-1]*=2
            if len(res)>=2:
                res[-2]*=2 
        elif i=="#": 
            res[-1]=res[-1]*(-1)
        else:
            if len(res)>=1:
                res.append(int(i))
                if res[-1]==0 and res[-2]==1:
                    res.pop()
                    res.pop()
                    res.append(10)
            else:
                res.append(int(i))
        print(res)
    return sum(res)
res=[]
#print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
