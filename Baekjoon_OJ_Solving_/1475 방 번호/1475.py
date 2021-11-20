import sys
input=sys.stdin.readline
n=input().rstrip().replace("6","9")
d=dict()
for i in n:
    d[i]=d.get(i,0)+1

if "9" in d:
    if d["9"]%2!=0:
        d["9"]=d["9"]//2+1
    else:
        d["9"]=d["9"]//2

d=sorted(d.items(),key=lambda x:-x[1])
print(d[0][1])

