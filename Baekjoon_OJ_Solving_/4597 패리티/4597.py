while 1:
    s=input().rstrip()
    if s=="#":
        break
    a=s.count("1")
    b=""
    if s[-1]=="e":
        if a%2==0:
            b=s[:len(s)-1]+"0"
        else:
            b=s[:len(s)-1]+"1"
    elif s[-1]=="o":
        if sum(map(int,s[:len(s)-1]))%2==0:
            b=s[:len(s)-1]+"1"
        else:
            b=s[:len(s)-1]+"0"
    print(b)