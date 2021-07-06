n=int(input())
for _ in range(n):
    s=input().rstrip()
    a=s.lower()
    g=a.count("g")
    b=a.count("b")
    if g>b:
        print("{} is GOOD".format(s))
    elif g==b:
        print("{} is NEUTRAL".format(s))
    else:
        print("{} is A BADDY".format(s))

    
