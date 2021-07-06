n=int(input())
for i in range(n):
    s=input()
    sum=0
    for j in s:
        if j.isalpha():
            a=ord(j)-64
            sum+=a
    if sum==100:
        print("PERFECT LIFE")
    else:
        print(sum)