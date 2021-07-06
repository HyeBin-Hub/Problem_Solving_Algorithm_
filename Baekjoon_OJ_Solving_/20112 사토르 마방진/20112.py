n=int(input())
arr=[input().rstrip() for _ in range(n)]
flag=0
for i in range(n):
    res=""
    for j in range(n):
        res+=arr[j][i]
    if arr[i]!=res:
        flag=1
        break
if flag:
    print("NO")
else:
    print("YES")
            