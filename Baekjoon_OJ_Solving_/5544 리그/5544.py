n=int(input())
score=[0]*(n+1)
for i in range(n*(n-1)//2):
    a,b,c,d=map(int,input().split())
    if c > d:
        score[a]+=3
        
    elif c==d:
        score[a]+=1
        score[b]+=1
        
    else:
        score[b]+=3
res=sorted(score,reverse=True)
for i in score[1:]:
    print(res.index(i)+1)
