# 별> 동그라미 > 네모 > 세모
# 다같으면 무승부
# 별 4  동그라미 3  네모 2   세모 1


import sys
input=sys.stdin.readline
n=int(input())
for _ in range(n):
    a=list(input().split())[1:]
    b=list(input().split())[1:]
    
    flag=0 

    for i in range(4,0,-1):
        i=str(i)
        if i in a and i in b:
            cnt_a=a.count(i)
            cnt_b=b.count(i)
            if cnt_a> cnt_b: 
                flag=1
                break
            elif cnt_a < cnt_b: 
                flag=0
                break            

        elif i not in b and i in a :
            flag=1
            break

        elif i in b and i not in a:
            flag=0
            break
        
        flag=2
    
    if flag==1:
        print("A")
    elif flag==2:
        print("D")
    else:
        print("B")

