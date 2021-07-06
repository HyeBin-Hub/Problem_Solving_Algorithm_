from collections import Counter,deque
while 1:
    n,m=map(int,input().split())
    if n==0:
        break
    ranking=[]
    for i in range(n):
       ranking.extend(list(map(int,input().split())))

    res=Counter(ranking)
    a=max(res.values())

    dic={}
    for key,val in res.items():
        if a!=val:
            dic[key]=val
    m=max(dic.values())
    
    tttt=[]
    for key,val in sorted(dic.items(),key=lambda x:x[0]):
        if m==val:
            tttt.append(key)
    print(" ".join(map(str,tttt)))