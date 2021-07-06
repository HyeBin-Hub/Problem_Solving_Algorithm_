arr=[int(input())for i in range(10)]
res=0
for i in arr:
    res+=i
    if res>=100:
        if res-100 > 100-(res-i):
            res-=i
        break
print(res)