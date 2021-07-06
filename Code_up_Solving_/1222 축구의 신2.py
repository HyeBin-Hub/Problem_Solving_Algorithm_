# 1 번째 방법
a,b,c=map(int,input().split())

if a%10==0:
    z=(90-a)//5
    q=z+b
else:
    z=(90-a)//5+1
    q=z+b

if q>c:
    print("win")
elif q<c:
    print("lose")
else:
    print("same")

# 2 번째 방법

minute, score ,score2= map(int, input().split())
 
while minute<90 :
    minute += 5
    score += 1
 
if score>score2:
    print("win")
elif score<score2:
    print("lose")
else:
    print("same")
