def abc(a):
    arr=int(str(a%10)+str((a%100)//10)+str(a//100))
    return arr
a=list(map(int,input().split()))
print(max([abc(i) for i in a]))