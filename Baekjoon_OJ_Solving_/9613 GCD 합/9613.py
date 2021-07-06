# a,b나 b,a가 같으므로 조합사용
from itertools import combinations
from math import gcd
t=int(input())
for _ in range(t):
    arr=list(combinations(list(map(int,input().split()))[1:],2))
    count=0
    for i in arr:
        count+=gcd(i[0],i[1])
    print(count)
