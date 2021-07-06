s=list(map(int,input().split()))
a=False
for i in range(len(s)):
    if s[i]%5==0:
        print(s[i])
        a=True
        break
if a==False:
    print(0)
        
