def run(save,visit):
    if len(save)==n:
        total=0
        for i in range(n-1):
            total+=abs(save[i]-save[i-1])
        result.append(total)
        return
    for i in range(n):
        if visit[i]:
            continue
        visit[i]=1
        run(save+[arr[i]],visit)
        visit[i]=0

n=int(input())
arr=list(map(int,input().split()))
result=[]
run([],[0]*n)
print(max(result))