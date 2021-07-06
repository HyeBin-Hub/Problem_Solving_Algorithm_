import sys
input=sys.stdin.readline
n,s=input().rstrip().split()
dic={}
for _ in range(int(n)):
    name,value=input().rstrip().split()
    dic[name]=value

count=0
for key,val in dic.items():
    if key==s:
        break
    if dic[s]==val:
        count+=1
print(count)
