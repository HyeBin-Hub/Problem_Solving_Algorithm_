n=int(input()) 
m=int(input()) 
targets=list(map(int,input().split()))
score=[0]*(n+1)

for i in range(m):
    arr=list(map(int,input().split()))
    for ind,j in enumerate(arr):
        if targets[i]==j:
            score[ind+1]+=1
        elif targets[i]!=j:
            score[targets[i]]+=1

for i in score[1:]:
    print(i)




