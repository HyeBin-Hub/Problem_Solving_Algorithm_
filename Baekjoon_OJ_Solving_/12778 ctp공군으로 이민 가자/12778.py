t=int(input())
for _ in range(t):
    m,s=input().rstrip().split()
    arr=input().rstrip().split()
    if s=="C":
        res=[]
        for i in arr:
            res.append(ord(i)-64)
        print(*res)
    elif s=="N":
        res=[]
        for  i in map(int,arr):
            res.append(chr(i+64))
        print(*res)



# ord : 문자에서 숫자고
# chr : 숫자에서 문자로   



