import sys
input=sys.stdin.readline
c,r=map(int,input().split())
n=int(input())
arr=[]
for i in range(n+1):
    d,p=map(int,input().split())
    if d==1: # 북
        arr.append(p)
    elif d==2: # 남
        arr.append(c+r+c-p)        
    elif d==3: # 서쪽
        arr.append(c+r+c+r-p)
    else: # 동
        arr.append(c+p)

m_arr=arr[-1]

res=0
for i in range(n):
     res+=min(abs(m_arr-arr[i]),((c+r)*2-abs(m_arr-arr[i])))
print(res)    
