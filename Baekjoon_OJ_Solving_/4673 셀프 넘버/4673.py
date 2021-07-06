def abc():
    res=[True]*10036
    for i in range(1,10000):
        res[i+(i//1000)+((i%1000)//100)+((i%100)//10)+(i%10)]=False
    for i in range(1,10000):
        if res[i]:
            print(i)
     
abc()