import sys
input=sys.stdin.readline
def run():
    n,m=map(int,input().split())
    dic_key={}
    dic_val=[]
    for i in range(1,n+1):
        a=input().rstrip()
        dic_val.append(a)
        dic_key[a]=i
    for i in range(m):
        a=input().rstrip()
        if a.isdigit():
            print(dic_val[int(a)-1])
        else:
            print(dic_key.get(a))
run()