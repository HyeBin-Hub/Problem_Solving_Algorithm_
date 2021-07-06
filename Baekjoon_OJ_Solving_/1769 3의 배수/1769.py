import sys
def run(a):
    global count

    if len(a)==1 :
        if int("".join(a))%3==0:
            print(count)
            print("YES")
            sys.exit()
        else:
            print(count)
            print("NO")
            sys.exit()

    total=0
    for i in a:
        total+=int(i)

    count+=1
    run(list(str(total)))
    
n=list(input().rstrip())
count=0

run(n)
