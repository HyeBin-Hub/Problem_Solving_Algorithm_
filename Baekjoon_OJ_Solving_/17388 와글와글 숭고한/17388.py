a,b,c=map(int,input().split())
arr=a+b+c
if arr>=100:
    print("OK")
else:
    if a==min(a,b,c):
        print("Soongsil")
    elif b==min(a,b,c):
        print("Korea")
    else:
        print("Hanyang ")