from collections import Counter
import sys
input=sys.stdin.readline
n=int(input())
arr=[list(map(int,input().split()))for _ in range(n)]
flag=0 

temp_list=[]
for i in arr:
    temp_list+=i
    
res=Counter(temp_list) 
temp=set(res.values())

if temp!={1}:
    print("FALSE")
    sys.exit()

sums=(n*(n**2+1))//2
                    

for row in arr:    
    if sums!=sum(row):
        flag=1 


for col in range(n):
    total=0
    for row in range(n):
        total+=arr[row][col]
    if total!=sums:
        flag=1

total_left=0
total_right=0

for i in range(n):
    total_left+=arr[i][i]
    total_right+=arr[i][n-i-1]

    if total_left==total_right!=sums:
        flag=1

if flag:
    print("FALSE")
else:
    print("TRUE")
        
