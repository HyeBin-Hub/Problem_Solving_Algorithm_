s=list(input())
count1=0
count2=0
for i in range(len(s)):
    if s[i]=="(":
        count1+=1
    else:
        count2+=1
print(count1,count2)
        
