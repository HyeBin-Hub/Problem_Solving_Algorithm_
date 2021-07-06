

import sys
input=sys.stdin.readline
n=int(input())
arr=[list(map(int,input().split()))for _ in range(n)]
player_score=[0]*n

for col in range(3):
    res=[]
    for row in range(n):
        res.append(arr[row][col])

    for row in range(n):
        if res.count(arr[row][col])==1:
            player_score[row]+=arr[row][col]
for i in player_score:
    print(i)    



    



        
    
