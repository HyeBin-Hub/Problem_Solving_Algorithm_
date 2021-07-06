

    
res=[0]*69
res[0]=1
res[1]=1
res[2]=2
res[3]=4
for i in range(4,69):
    res[i]=res[i-1]+res[i-2]+res[i-3]+res[i-4]
for i in range(int(input())):
    print(res[int(input())])
