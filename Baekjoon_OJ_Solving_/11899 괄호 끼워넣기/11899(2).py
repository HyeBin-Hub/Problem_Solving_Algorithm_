s=input()
a,b=0,0
for i in s:
    if i=="(":
        a+=1
    else:
        if a==0:
            b+=1
        else:
            a-=1
print(a+b)


s=input()
arr=[]
for i in s:
    if i=="(":
        arr.append(i)
    else:
        if len(arr)==0 or arr[-1]==")":
            arr.append(i)
        else:
            arr.pop()
print(len(arr))