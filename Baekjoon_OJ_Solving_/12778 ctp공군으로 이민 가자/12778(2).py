t=int(input())
for _ in range(t):
    m,s=input().rstrip().split()
    arr=input().rstrip().split()
    if s=="C":
        for i in arr:
            print(ord(i)-64,end=" ")

    elif s=="N":
        for  i in map(int,arr):
            print(chr(i+64),end=" ")
    print()