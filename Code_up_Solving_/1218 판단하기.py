
a,b,c=map(int,input().split())
if a+b>c:
    if a==b==c:
        print("정삼각형")
    elif a==b or a==c or b==c:
        print("이등변삼각형")
    elif a*a+b*b==c*c:
        print("직각삼각형")
    else:
        print("삼각형")
else:
    print("삼각형아님")
