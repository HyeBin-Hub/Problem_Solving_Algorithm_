s=input().rstrip()
p=""
i=0
while i<len(s):
    p+=s[i]
    if s[i] in "aeiou":
        i+=3
    else:
        i+=1
print(p)