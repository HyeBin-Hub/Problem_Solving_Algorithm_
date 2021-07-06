s=input()
for i in range(len(s)):
    if s[i]=="+":
        a=int(s[:i])
        b=int(s[i+1:])
        print(a+b)
    elif s[i]=="-":
        a=int(s[:i])
        b=int(s[i+1:])
        print(a-b)
    elif s[i]=="*":
        a=int(s[:i])
        b=int(s[i+1:])
        print(a*b)
    elif s[i]=="/":
        a=int(s[:i])
        b=int(s[i+1:])
        print(round(a/b,2))
        
        
