from collections import Counter
n=input().upper()
a=Counter(n)
t=max(a.values())
count=0
for k,v in a.items():
    if v==t:
        b=k
        count+=1

if count>=2:
    print("?")
else:
    print(b)