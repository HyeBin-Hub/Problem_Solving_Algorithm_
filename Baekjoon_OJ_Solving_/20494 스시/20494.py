n=int(input())
count=0
for _ in range(n):
    s=input().rstrip()
    count+=len(s)
print(count)