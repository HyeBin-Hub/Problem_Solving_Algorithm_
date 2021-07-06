import sys
def run(j,total):
    global maximum,minimum
    if sum(cnt)==n-1:
        maximum=max(total,maximum)
        minimum=min(total,minimum)
        return
    
    for i in ("+-*%"):
        if i=="+":
            if signs[0]>cnt[0]:
                cnt[0]+=1
                run(j+1,total+a[j])
                cnt[0]-=1
        elif i=="-":
            if signs[1]>cnt[1]:
                cnt[1]+=1
                run(j+1,total-a[j])
                cnt[1]-=1
        elif i=="*":
            if signs[2]>cnt[2]:
                cnt[2]+=1
                run(j+1,total*a[j])
                cnt[2]-=1
        elif i=="%":
            if signs[3]>cnt[3]:
                cnt[3]+=1
                if total<0:
                    run(j+1,-(abs(total)//a[j]))
                    cnt[3]-=1
                else:
                    run(j+1,total//a[j])
                    cnt[3]-=1
        
n=int(input())
a=list(map(int,input().split()))
signs=list(map(int,input().split()))
cnt=[0]*4
maximum=0
minimum=sys.maxsize
run(1,a[0])
print(maximum)
print(minimum)