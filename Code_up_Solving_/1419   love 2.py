s=input()
count=0
for i in range(len(s)-4):
    if s[i:i+4]=="love":
        count+=1
print(count)
    
