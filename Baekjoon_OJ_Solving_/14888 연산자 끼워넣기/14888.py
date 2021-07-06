import sys
def run(num,cnt):
    global mins,maxs
    if cnt==n:
        mins=min(num,mins)
        maxs=max(num,maxs)
        return

    if sign_cnt[0]>0: # +
        sign_cnt[0]-=1
        run(num+a[cnt],cnt+1)
        sign_cnt[0]+=1

    if sign_cnt[1]>0: # -
        sign_cnt[1]-=1
        run(num-a[cnt],cnt+1)
        sign_cnt[1]+=1

    if sign_cnt[2]>0: # *
        sign_cnt[2]-=1
        run(num*a[cnt],cnt+1)
        sign_cnt[2]+=1

    if sign_cnt[3]>0: # //
        res=abs(num)//a[cnt]
        if num<0:
            res*=-1
        sign_cnt[3]-=1
        run(res,cnt+1)
        sign_cnt[3]+=1

n=int(input())
a=list(map(int,input().split()))
sign_cnt=list(map(int,input().split()))
mins=10**9
maxs=-10**9
run(a[0],1)
print(maxs)
print(mins)