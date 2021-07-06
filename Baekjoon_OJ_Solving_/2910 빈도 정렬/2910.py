from collections import Counter
n,c=map(int,input().split())
arr=list(input().rstrip().split())
res=Counter(arr)
res=sorted(res.items(),key=lambda x:x[1],reverse=True)
answer=""
for i in res:
    for _ in range(i[1]):
        answer+=str(i[0])+" "
print(answer[:-1])