c,k=map(float,input().split())
st=(c-100)*0.9
big=(k-st)*100/st
if big<=10:
    print("정상")
elif big<=20:
    print("과체중")
else:
    print("비만")
