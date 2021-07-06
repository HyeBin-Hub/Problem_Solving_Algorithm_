n=int(input())
first=""
seconde=""
for _ in range(n):
    s=input().rstrip()
    if len(s)%2!=0:
        s=s*2
    first=""
    seconde=""
    for i in range(len(s)):
        if i%2==0:
            first+=s[i]
        else:
            seconde+=s[i]
    print(first)
    print(seconde)
            

    