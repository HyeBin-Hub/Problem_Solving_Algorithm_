# 1 번째 방법

y,m=map(int,input().split())
if y%4==0 and y%100!=0 or y%400==0:
    if m==2:
        print(29)
    else:
        if m<8 and m%2!=0 or m>=8 and m%2==0:
            print(31)
        else:
            print(30)     
else:
    if m==2:
        print(28)
    else:
        if m<8 and m%2!=0 or m>=8 and m%2==0:
            print(31)
        else:
            print(30)

# 2 번째 방법   

year, month = input().split()
year = int(year)
month = int(month)
february = 0
​
if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
    february = 29
else:
    february = 28
​
if(month < 8):
    if(month == 2):
        print(february)
    elif(month % 2 == 0):
        print('30')
    else:
        print('31')
else:
    if(month % 2 == 0):
        print('31')
    else:
        print('30')
​







