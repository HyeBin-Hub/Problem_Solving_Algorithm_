arr=sorted([int(input())for _ in range(int(input()))],reverse=True)
cnt=0
for ind,i in enumerate(arr,1):
    a=i-(ind-1)
    if a>=0:
        cnt+=a
print(cnt)
   


