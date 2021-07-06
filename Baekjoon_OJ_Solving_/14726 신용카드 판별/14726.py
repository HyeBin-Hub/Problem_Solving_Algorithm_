t=int(input())
for _ in range(t):
    number=list(input().rstrip())
    number=list(map(int,number[::-1]))

    for i in range(1,17,2):
        if int(number[i])*2 >= 10:
            number[i]=int(number[i])*2//10+int(number[i])*2%10
        else:
            number[i]=int(number[i])*2 
            
    if sum(number)%10:
        print("F")
    else:
        print("T")