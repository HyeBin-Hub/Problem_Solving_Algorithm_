
r,c=map(int,input().split())
board=[list(map(int,input().split()))for i in range(r)]
t=int(input())
cnt=0
for i in range(r-2):
    f_1=board[i]
    f_2=board[i+1]
    f_3=board[i+2]
    for j in range(c-2):
        if sorted(f_1[j:j+3]+f_2[j:j+3]+f_3[j:j+3])[4]>=t:
            cnt+=1
print(cnt)
