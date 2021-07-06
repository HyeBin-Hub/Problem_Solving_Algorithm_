import sys

def run(total):
    global count
    if len(total)==1:
        print(count)
        a=list(map(int,total))
        print("NO "if a[0]%3 else "YES")
        sys.exit()

    total=sum(map(int,total))
    count+=1
    run(list(str(total)))

input=sys.stdin.readline
x=list(input().rstrip())
count=0
run(x)