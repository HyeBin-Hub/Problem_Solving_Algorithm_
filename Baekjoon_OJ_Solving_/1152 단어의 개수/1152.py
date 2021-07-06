arr=input()
count=0
for i in arr.split(" "):
    if i=="":
        continue
    else:
        count+=1
print(count)
