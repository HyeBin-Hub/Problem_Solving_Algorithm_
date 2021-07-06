import sys
input=sys.stdin.readline

n=int(input())
total=0
for i in range(n):
    hm,dd=input().split()
    hh,mm=map(int,hm.split(":"))
    cost=0
    for i in range(int(dd)):
        if 7<=hh<19:
            cost+=10
        else:
            cost+=5
        mm+=1

        if mm==60:
            hh+=1
            if hh==24:
                hh=0
            mm=0
    total+=cost
print(total)
