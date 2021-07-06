def back(result):
    if len(result)==m:
        print(*result)
        return
    for i in range(1,n+1):
        if i not in result:
            back(result+[i])
            
n,m=map(int,input().split())
result=[]
back(result) 








