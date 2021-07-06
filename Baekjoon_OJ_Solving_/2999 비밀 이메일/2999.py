


s=input().rstrip()
n=len(s)
for i in range(1,n+1):
    j=n//i

    if i<=j and i*j==n:
        r=i

for i in range(r):
    print(s[i::r],end= "")
