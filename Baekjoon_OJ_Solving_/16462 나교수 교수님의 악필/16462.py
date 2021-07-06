n=int(input())
total=0
for _ in range(n):
    score=input().rstrip()
    if score!="100":
        a=score.replace("6","9").replace("0","9")

        total+=int(a)
    else:
        total+=int(score)

if (total/n*10)%10 <5:
    print(total//n)
else:
    print(total//n+1)

