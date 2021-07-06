s=input().rstrip()
res=[]
for i in range(len(s)-2):
    for j in range(len(s)-2):
        if s[i+1:-j-1]:
            res.append(s[:i+1][::-1]+s[i+1:-j-1][::-1]+s[-j-1:][::-1])

print(sorted(res)[0])    

print("5")