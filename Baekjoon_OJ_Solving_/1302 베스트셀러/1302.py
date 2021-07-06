n=int(input())
dic={}
for _ in range(n):
    s=input().rstrip()
    dic[s]=dic.get(s,0)+1

# res=sorted(dic.items(),key=lambda x:(-x[1],x[0]))
print(sorted(dic.items(),key=lambda x:(-x[1],x[0]))[0][0])
