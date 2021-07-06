def run(start,end,length):
    if length==1:
        return
    a=(end-start)//3
    frist=start+a
    second=start+a*2
    for i in range(frist,second):
        s[i]=" "
    run(start,frist,length//3)
    run(second,end,length//3)
import sys
for i in sys.stdin:
    n=int(i)
    #total=3**n
    s=list("-"*(3**n))
    run(0,len(s),len(s))
    print("".join(s))