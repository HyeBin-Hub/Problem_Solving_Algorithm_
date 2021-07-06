

from collections import Counter
s=input().rstrip()
a=Counter(s)
res=sorted(a.items(),key=lambda x:x)

a=s.split(res[0][0])

count=0
for i in a:
    if i!="":
        count+=1
print(count) 


