s=input()
s=s.lower()
count=0
count2=0
for i in range(len(s)):
    if s[i]=="c":
        count+=1
    if s[i:i+2]=="cc":
        count2+=1
        
print(count,count2)
