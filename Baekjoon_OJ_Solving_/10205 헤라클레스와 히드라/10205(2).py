for i in range(int(input())):
    n1=int(input())
    s1=input().rstrip()
    for j in s1:
        if j=="c":
            n1+=1
        else:
            n1-=1

    print("Data Set {}:".format(i+1))
    print(n1,"\n")
