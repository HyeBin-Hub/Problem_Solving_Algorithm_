import sys
input=sys.stdin.readline
n=int(input())
for _ in range(n):
    num=list(input().rstrip())
    count=0
    if num==list("6174"):
        print(count)
        continue
    total=num
    while 1:
        total.sort()

        max_n="".join(reversed(total))
        min_n="".join(total)

        total=str(int(max_n)-int(min_n)).zfill(4)

        if total=="6174":
            print(count+1)
            break
        else:
            count+=1 
            total=list(total)   