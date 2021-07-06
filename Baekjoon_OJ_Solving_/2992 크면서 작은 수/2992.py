import sys
input=sys.stdin.readline
def run(save,count):
    global minimum
    if len(save)==len(x) :
        if int("".join(save))>int("".join(x))  :
            minimum=min(int("".join(save)),minimum)
            return
    
    for i in range(len(x)):
        if count[i]==0:
            count[i]+=1
            run(save+[x[i]],count)
            count[i]-=1

x=list(input().rstrip())

minimum=sys.maxsize
count=[0]*len(x)

if x.count(x[0])==len(x):
    print(0)
    sys.exit()
else:
    run([],count)
    if  minimum!=sys.maxsize:
        print(minimum)
    else:
        print(0)    

