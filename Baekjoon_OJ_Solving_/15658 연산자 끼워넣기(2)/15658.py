import sys
def run(ind,res):
    global maximum,minimum
    if ind==n-1:
        maximum=max(res,maximum)
        minimum=min(res,minimum)
        return
    for sign_ind in range(4):
        if count[sign_ind]<signs[sign_ind]:
            count[sign_ind]+=1

            if sign_ind==0: # +
                run(ind+1,res+a[ind+1])
            elif sign_ind==1: # -
                run(ind+1,res-a[ind+1])
            elif sign_ind==2: # *
                run(ind+1,res*a[ind+1])
            elif sign_ind==3 :
                if res<0:
                    run(ind+1,-(-res//a[ind+1]))
                else:
                    run(ind+1,res//a[ind+1])
            count[sign_ind]-=1



n=int(input())
a=list(map(int,input().split()))
signs=list(map(int,input().split()))
count=[0,0,0,0]
maximum=-45
minimum=45
run(0,a[0])
print(maximum)
print(minimum)