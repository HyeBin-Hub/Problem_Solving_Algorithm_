def abc(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return abc(n-1)+abc(n-2)
n=int(input())
print(abc(n))