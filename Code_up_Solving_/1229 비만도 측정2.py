h,w=map(float,input().split())
if h<150:
    st=h-100
elif h<160:
    st=(h-150)/2+50
else:
    st=(h-100)*0.9
big=(w-st)*100/st
if big<=10:
    print("정상")
elif big <=20:
    print("과체중")
else:
    print("비만")
    
