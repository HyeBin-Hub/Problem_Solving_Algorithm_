n=int(input())
for i in range(n):
    arr=input()
    count=0
    sum=0
    for j in arr:
        if j=="O":
            count+=1
            sum+=count
        elif j=="X":
            count=0  
    print(sum)
