t=int(input())
for _ in range(t):
    a,b=input().rstrip().split()
    one,zero=0,0
    for i,j in zip(a,b):
        if i!=j:
            if i=="1":
                one+=1
            else:
                zero+=1
    print(max(one,zero))


