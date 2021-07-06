import sys
input=sys.stdin.readline
def run(save,count):
    global flag,num

    if len(save)==len(x) :
        num+=1
        if num==ind:
            flag=1
            print("{} {} = {}".format(x,ind,"".join(save)))
            return
    if flag:
        return
        
    for i in range(len(x)):
        if count[i]==0:
            count[i]+=1
            run(save+[x[i]],count)
            count[i]-=1

for i in sys.stdin:
    x,ind=i.split()
    ind=int(ind)
    count=[0]*len(x)
    flag=0
    num=0
    run([],count)
    if flag==0:
        print("{} {} = {}".format(x,ind,"No permutation"))