s=input().rstrip()
stack_total=[]
total=0
for i in range(len(s)):
    if s[i].isalpha():

        if s[i]=="H":
            total+=1
        elif s[i]=="C":
            total+=12
        elif s[i]=="O":
            total+=16
        
    elif s[i].isdigit():
        total*=int(s[i])
    elif s[i]=="(":
        stack_total.append(total)
        total=0
print(sum(stack_total)+total)
    
    #if s[i].isdigit():
        

