n,m=map(int,input().split())
arr=[list(map(int,input()))for _ in range(n)]

res=[] # 정사각형 크기 담을 리스트

for ind,row in enumerate(arr):
    if ind<n-1:
        for i in range(m-1):
            for j in range(i+1,m):
                if row[i]==row[j]:
                    lenght=j-i
                    if lenght<=n-1:
                        if arr[ind+lenght][i]==row[i] and arr[ind+lenght][j]==row[j]:
                            res.append((lenght+1)*(lenght+1))
                    
print(max(res))

