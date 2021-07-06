s=list(input().rstrip())
alp=[3,	2	,1	,2	,3	,3	,3	,3	,1	,1	,3	,1	,3	,3	,1	,2	,2	,2	,1	,2	,1	,1	,2	,2	,2	,1]

arr=[]
if len(s)%2:
    for i in range(0,len(s)-1,2):
        arr.append((alp[ord(s[i])-65]+alp[ord(s[i+1])-65])%10)
    arr.append((alp[ord(s[-1])-65])%10)
else:
    for i in range(0,len(s),2):
        arr.append((alp[ord(s[i])-65]+alp[ord(s[i+1])-65])%10)

while len(arr)!=1:
    if len(arr)%2:
        res=[]
        for i in range(0,len(arr)-1,2):
            res.append((arr[i]+arr[i+1])%10)
        res.append((arr[-1])%10)
    else:
        res=[]
        for i in range(0,len(arr),2):
            res.append((arr[i]+arr[i+1])%10)
    arr=res

if arr[0]%2==0 or arr[0]==0:
    print("You're the winner?")
else:
    print("I'm a winner!")

