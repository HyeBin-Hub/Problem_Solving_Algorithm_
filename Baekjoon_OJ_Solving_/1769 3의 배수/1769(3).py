import sys

def run(x):
    global count
    if len(x)==1:
        print(count)
        print("NO" if int("".join(x))%3 else "YES")
        sys.exit()
    sums=list(str(sum(map(int,x))))

    count+=1
    run(sums)
    
x=list(input().rstrip())
count=0
run(x)
