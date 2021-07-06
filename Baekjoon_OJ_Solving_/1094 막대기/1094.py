import sys
input=sys.stdin.readline
x=int(input())
bar=64
count=0
while x!=0:
    if x>=bar:
        count+=1
        x-=bar
    bar//=2
print(count)
