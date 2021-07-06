s=input().rstrip()
n=int(input())
count=0
for i in range(n):
    a=input().rstrip()*2
    if s in a:
        count+=1
print(count)