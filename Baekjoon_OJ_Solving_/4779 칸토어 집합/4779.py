import sys
def run(start,end,length):
    if length==1:
        return
    
    a=(end-start)//3
    first=start + a
    second=start + a * 2

    for i in range(first,second):
        s[i]=" "

    run(start,first,length//3)
    run(second,end,length//3)


for i in sys.stdin:
    n=int(i)

    total=3**n

    s=list("-"*total)

    run(0,total,total)

    print(''.join(s))