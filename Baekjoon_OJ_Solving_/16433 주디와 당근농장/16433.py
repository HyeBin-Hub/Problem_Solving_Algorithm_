n,r,c=map(int,input().split())
s=[[0]*n for i in range(n)]    
for i in range(n):
    for j in range(n):
        if r%2==0 and c%2==1 or r%2==1 and c%2==0:
            if i%2==1 and j%2==0 or i%2==0 and j%2==1:
                s[i][j]="v"
            else:
                s[i][j]="."
        else:
            if i%2==1 and j%2==0 or i%2==0 and j%2==1:
                s[i][j]="."
            else:
                s[i][j]="v"

for i in range(n):
    for j in range(n):
        print(s[i][j],end="")
    print()