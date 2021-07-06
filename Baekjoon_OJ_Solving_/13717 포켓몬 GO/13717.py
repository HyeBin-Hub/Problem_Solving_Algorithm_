n=int(input())
dic={}
for i in range(n):
    pi=input().rstrip()
    ki,mi=map(int,input().split())
    cnt=0
    while mi>=ki:
        mi-=ki
        mi+=2
        cnt+=1
    dic[pi]=cnt


print(sum(dic.values()))
print(sorted(dic.items(),key=lambda x:x[1],reverse=True)[0][0])