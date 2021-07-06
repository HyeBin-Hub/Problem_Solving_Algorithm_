# 1등 당첨번호 6개 일치
# 2등 당첨번호 5개 일치 + 보너스 번호 일치
# 3등 5개번호 일치
# 4등 4개번호 일치
# 5등 3개 번호 일치
# 꽝 2개 번호 일치

f=list(map(int,input().split()))
m=list(map(int,input().split()))
arr=f[0:6]
count=0
for i in arr:
    for j in m:
        if i==j:
            count+=1

a=False
if count==6:
    print(1)
elif count==5:
    for i in m:
        if f[-1]==i:
            a=True
            break  
        else:
            a=False
    if a==True:
        print(2)
    else:
        print(3)
            
elif count==4:
    print(4)
elif count==3:
    print(5)
else:
    print(0)

    
"""
# test case add
14 15 23 25 35 43 32
23 15 35 32 43 14 

"""
    
