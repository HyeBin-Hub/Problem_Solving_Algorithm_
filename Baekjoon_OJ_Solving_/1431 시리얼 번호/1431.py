n=int(input())
dic=[]
for i in range(n):
    s=input().rstrip()
    total=0
    for j in s:
        if j.isdigit():
            total+=int(j)
    dic.append((list(s),total))


res=sorted(dic,key=lambda x:(len(x[0]),x[1],x[0]))
for i in res:
    print("".join(i[0]))