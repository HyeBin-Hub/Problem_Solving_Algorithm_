
import sys
for i in range(int(input())):
    p=input().rstrip().replace("RR","")
    n=int(input())
    a=input().rstrip()[1:-1].split(",")
    r_cnt=0
    f_cnt=0
    b_cnt=0
    for i in p:
        if i=="R":
            r_cnt+=1
        elif i=="D":
            if r_cnt%2==0:
                f_cnt+=1
            else:
                b_cnt+=1

    if f_cnt+b_cnt<=n:
        a=a[f_cnt:n-b_cnt]

        if r_cnt%2==1:
            print("["+",".join(a[::-1])+"]")
        else:
            print("["+",".join(a)+"]")
    else:
        print("error")