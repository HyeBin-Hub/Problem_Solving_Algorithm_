def run(save,visit):
    global count
    if len(save)==n:
        total=500
        flag=0
        for i in save:
            total+=(i-k)
            if total<500:
                flag=1
                break
        if flag:
            return
        else:
            count+=1
            return

    for i in range(n):
        if visit[i]:
            continue
        visit[i]=1
        save.append(arr[i])
        run(save,visit)
        visit[i]=0
        save.pop()

n,k=map(int,input().split())
arr=list(map(int,input().split()))
visit=[0]*n
save=[]
count=0
run(save,visit)
print(count)