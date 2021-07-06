import sys 
input=sys.stdin.readline
n=int(input())
for _ in range(n):
    p=int(input())
    dic={}
    for _ in range(p):
        price,name=input().rstrip().split()
        dic[name]=int(price)
    maximum=max(dic.values())
    for k,v in dic.items():
        if v==maximum:
            print(k)