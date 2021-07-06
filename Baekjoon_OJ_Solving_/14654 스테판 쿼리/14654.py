import sys
input=sys.stdin.readline
n=int(input())
a_play=list(map(int,input().split()))
b_play=list(map(int,input().split()))
win=[(1,2),(2,3),(3,1)]
w=0 
res=0
maxs=0
for i in range(n):
    if (a_play[i],b_play[i]) in win:
        if w==0:
            w=1
            res=1
        else:
            res+=1
    elif a_play[i]==b_play[i]:
        if w==0:
            w=1
            res=1
        else:
            w=0  
            res=1
    else:
        if w==1:
            w=0
            res=1
        else:
            res+=1
    maxs=max(res,maxs)
print(maxs)  